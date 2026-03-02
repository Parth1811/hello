#!/usr/bin/env python3
"""Tkinter-based shortcut launcher — near-instant startup, same UX as the pygame version.

Usage:
    python -m shortcuts_app.app          # GUI mode
    python -m shortcuts_app.app 12       # CLI: drill into group 1, pick item 2
"""

import os
import sys
import tkinter as tk
from copy import deepcopy
from typing import List, Union

from PIL import Image, ImageTk

from .models import (
    ShortcutLink, ShortcutGroup, SHORTCUT_REGISTRY, is_group,
)
from .launcher import (
    launch_shortcut, FORMAT_INPUT_NAMES, INDEX_INPUT_NAMES,
)

# ---------------------------------------------------------------------------
# Display constants
# ---------------------------------------------------------------------------

APP_WIDTH = 800
APP_HEIGHT = 600
BG_COLOR = "#1e88e5"       # Blue — matches pygame BLUE (30, 136, 229)
TEXT_COLOR = "#000000"      # Black — matches pygame BLACK
HEADER_COLOR = "#000000"   # White — matches pygame BLACK
SELECTED_COLOR = "#ff8f00"
MENU_BG_COLOR = "#1e88e5"  # Blue background behind menu item text
STATUS_BG_COLOR = "#1e88e5"
FONT_FAMILY = "Helvetica"
FONT_SIZE = 28
HEADER_FONT_SIZE = 30

# Path to background image (lives in parent shortcuts/ directory)
_PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
_BG_IMAGE_PATH = os.path.join(_PACKAGE_DIR, '..', 'firefox.jpg')


# ---------------------------------------------------------------------------
# Input prompt dialog (replaces pygame prompt_for_input)
# ---------------------------------------------------------------------------

class InputDialog:
    """Small popup for dynamic input (ticket numbers, env selectors)."""

    def __init__(self, parent, title="Enter input"):
        self.result = None
        self.top = tk.Toplevel(parent)
        self.top.title(title)
        self.top.geometry("300x80")
        self.top.resizable(False, False)
        self.top.grab_set()

        self.entry = tk.Entry(self.top, font=(FONT_FAMILY, FONT_SIZE))
        self.entry.pack(fill=tk.X, padx=10, pady=(10, 5))
        self.entry.focus_set()
        self.entry.bind("<Return>", self._on_submit)
        self.entry.bind("<Escape>", lambda e: self.top.destroy())

    def _on_submit(self, event=None):
        self.result = self.entry.get()
        self.top.destroy()

    def wait(self):
        self.top.wait_window()
        return self.result


# ---------------------------------------------------------------------------
# Main application window
# ---------------------------------------------------------------------------

class ShortcutApp:
    def __init__(self):
        self.active_menu: List[Union[ShortcutLink, ShortcutGroup]] = deepcopy(SHORTCUT_REGISTRY)
        self.parent_menu = None
        self.child_menu_cache = None
        self.current_group_name = ''
        self.selected_index = -1
        self.selected_name = ''

        self.root = tk.Tk()
        self.root.title("Shortcut Launcher")
        self.root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.root.resizable(False, False)

        # Center the window on screen
        self.root.update_idletasks()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w - APP_WIDTH) // 2
        y = (screen_h - APP_HEIGHT) // 2
        self.root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{x}+{y}")

        # Force window to front and grab focus (macOS needs the extra lift/attributes)
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.after(100, lambda: self.root.attributes("-topmost", False))
        self.root.focus_force()

        # Background image on a canvas
        self.canvas = tk.Canvas(self.root, width=APP_WIDTH, height=APP_HEIGHT,
                                highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Load and scale background image
        self._bg_photo = None
        if os.path.exists(_BG_IMAGE_PATH):
            bg_img = Image.open(_BG_IMAGE_PATH).resize((APP_WIDTH, APP_HEIGHT), Image.LANCZOS)
            self._bg_photo = ImageTk.PhotoImage(bg_img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self._bg_photo)
        else:
            self.canvas.configure(bg=BG_COLOR)

        # Header text on canvas (with tight background box)
        self._header_id = self.canvas.create_text(
            APP_WIDTH // 2, 25, text="Please select a Website to be launched",
            font=(FONT_FAMILY, HEADER_FONT_SIZE, "bold"), fill=HEADER_COLOR,
        )
        # Measure text then add bg box behind it
        hbox = self.canvas.bbox(self._header_id)
        self._header_bg_id = self.canvas.create_rectangle(
            hbox[0] - 6, hbox[1] - 3, hbox[2] + 6, hbox[3] + 3,
            fill=MENU_BG_COLOR, outline="",
        )
        self.canvas.tag_lower(self._header_bg_id, self._header_id)

        # Status text at bottom (with tight background box)
        self._status_id = self.canvas.create_text(
            APP_WIDTH // 2, APP_HEIGHT - 25, text="Selected: (none)",
            font=(FONT_FAMILY, FONT_SIZE, "bold"), fill=TEXT_COLOR,
        )
        sbox = self.canvas.bbox(self._status_id)
        self._status_bg_id = self.canvas.create_rectangle(
            sbox[0] - 6, sbox[1] - 3, sbox[2] + 6, sbox[3] + 3,
            fill=STATUS_BG_COLOR, outline="",
        )
        self.canvas.tag_lower(self._status_bg_id, self._status_id)

        # Track menu item canvas IDs for click binding and refresh
        self._menu_item_ids: list = []

        # Key bindings — number keys 1-9
        for i in range(1, 10):
            self.root.bind(str(i), self._make_select_handler(i - 1))
            self.root.bind(f"<KP_{i}>", self._make_select_handler(i - 1))

        self.root.bind("<Return>", self._on_enter)
        self.root.bind("<KP_Enter>", self._on_enter)
        self.root.bind("<Left>", self._on_left)
        self.root.bind("<Right>", self._on_right)
        self.root.bind("<Down>", self._on_quit)
        self.root.bind("q", self._on_quit)
        self.root.bind("<Escape>", self._on_quit)

        self._refresh_display()

    def _make_select_handler(self, index):
        def handler(event):
            self._select(index)
        return handler


    def _select(self, index):
        if index >= len(self.active_menu):
            return
        entry = self.active_menu[index]
        if is_group(entry):
            self.current_group_name = entry.name
            self.parent_menu = self.active_menu
            self.active_menu = entry.children
            self.child_menu_cache = None
            self.selected_index = -1
            self.selected_name = ''
            self._refresh_display()
        else:
            self.selected_index = index
            self.selected_name = entry.name
            self._update_status()

    def _on_enter(self, event=None):
        if self.selected_index == -1:
            return
        entry = self.active_menu[self.selected_index]

        # Handle entries that need dynamic input
        if entry.name in FORMAT_INPUT_NAMES:
            user_input = InputDialog(self.root, "Enter value").wait()
            if user_input:
                entry = ShortcutLink(name=entry.name, url=entry.url % user_input)
                self.active_menu[self.selected_index] = entry

        if entry.name in INDEX_INPUT_NAMES:
            user_input = InputDialog(self.root, "Enter index").wait()
            if user_input:
                entry = ShortcutLink(name=entry.name, url=entry.children[int(user_input)].url)
                self.active_menu[self.selected_index] = entry

        launch_shortcut(entry)
        self.root.destroy()

    def _on_left(self, event=None):
        if self.parent_menu is None:
            return
        if self.current_group_name != '':
            self.child_menu_cache = ShortcutGroup(
                name=self.current_group_name, children=self.active_menu
            )
        else:
            self.child_menu_cache = None
        self.active_menu = self.parent_menu
        self.parent_menu = None
        self.current_group_name = ''
        self.selected_index = -1
        self.selected_name = ''
        self._refresh_display()

    def _on_right(self, event=None):
        if self.child_menu_cache is None:
            return
        self.current_group_name = self.child_menu_cache.name
        self.parent_menu = self.active_menu
        self.active_menu = self.child_menu_cache.children
        self.child_menu_cache = None
        self.selected_index = -1
        self.selected_name = ''
        self._refresh_display()

    def _on_quit(self, event=None):
        self.root.destroy()


    def _refresh_display(self):
        """Rebuild the menu item text on the canvas."""
        # Update header
        group_prefix = f"{self.current_group_name} " if self.current_group_name else ""
        self.canvas.itemconfig(
            self._header_id,
            text=f"Please select the {group_prefix}Website to be launched",
        )
        # Re-fit header background box
        hbox = self.canvas.bbox(self._header_id)
        self.canvas.coords(self._header_bg_id,
                           hbox[0] - 6, hbox[1] - 3, hbox[2] + 6, hbox[3] + 3)

        # Remove old menu item texts and backgrounds
        for item_id in self._menu_item_ids:
            self.canvas.delete(item_id)
        self._menu_item_ids.clear()

        # Draw menu items with tight background boxes
        for i, entry in enumerate(self.active_menu):
            label_text = f"{i + 1}) {entry.name}"
            y_pos = 75 + i * 45

            # Draw text first to measure it
            item_id = self.canvas.create_text(
                35, y_pos, text=label_text, anchor="w",
                font=(FONT_FAMILY, FONT_SIZE, "bold"), fill=TEXT_COLOR,
            )
            # Measure and create tight bg box
            tbox = self.canvas.bbox(item_id)
            bg_id = self.canvas.create_rectangle(
                tbox[0] - 4, tbox[1] - 2, tbox[2] + 4, tbox[3] + 2,
                fill=MENU_BG_COLOR, outline="",
            )
            # Push bg behind text
            self.canvas.tag_lower(bg_id, item_id)

            self._menu_item_ids.append(bg_id)
            self._menu_item_ids.append(item_id)

            # Click to select (bind both bg rect and text)
            self.canvas.tag_bind(bg_id, "<Button-1>",
                                 lambda e, idx=i: self._select(idx))
            self.canvas.tag_bind(item_id, "<Button-1>",
                                 lambda e, idx=i: self._select(idx))

        self._update_status()

    def _update_status(self):
        name = self.selected_name if self.selected_name else "(none)"
        self.canvas.itemconfig(self._status_id, text=f"Selected: {name}")
        # Re-fit status background box
        sbox = self.canvas.bbox(self._status_id)
        self.canvas.coords(self._status_bg_id,
                           sbox[0] - 6, sbox[1] - 3, sbox[2] + 6, sbox[3] + 3)

    def run(self):
        self.root.mainloop()


# ---------------------------------------------------------------------------
# CLI shortcut mode (e.g. `python -m shortcuts_app.app 12`)
# ---------------------------------------------------------------------------

def cli_mode(arg: str):
    """Drill through groups and launch without GUI."""
    menu = deepcopy(SHORTCUT_REGISTRY)
    selected_index = -1

    for char in arg:
        idx = int(char) - 1
        entry = menu[idx]
        if is_group(entry):
            menu = entry.children
            continue
        selected_index = idx

    if selected_index != -1:
        launch_shortcut(menu[selected_index])


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) > 1:
        cli_mode(sys.argv[1])
    else:
        app = ShortcutApp()
        app.run()


if __name__ == "__main__":
    main()
