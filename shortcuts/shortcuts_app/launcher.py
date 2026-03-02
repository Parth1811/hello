"""Shared launch / action logic — no UI dependency."""

import os
from typing import List, Union

from .models import ShortcutLink, ShortcutGroup


def launch_shortcut(entry: ShortcutLink):
    """Open a shortcut link. Handles Macros, Passwords, and regular URLs."""
    if entry.name.startswith("Macro:"):
        os.popen(f"echo '{entry.url}' | pbcopy")
        return

    if entry.name.startswith("PWD"):
        os.popen(f"echo '{os.environ[entry.url]}' | pbcopy")
        return

    url = entry.url
    # os.system('nohup google-chrome ' + url + ' >/dev/null 2>&1 &')
    # os.system(f'open -a "Google Chrome" "{url}"')
    os.system(f'open "{url}"')
    # os.system(f'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" {url}')


# Names that need dynamic input before launching (format string with %s)
FORMAT_INPUT_NAMES = frozenset({
    'Django tickets', 'RTD Issues', 'SNARE Issues', 'TANNER Issues', 'Drivetrain',
})

# Names that need index-based selection input
INDEX_INPUT_NAMES = frozenset({
    'Vocab Lists',
})
