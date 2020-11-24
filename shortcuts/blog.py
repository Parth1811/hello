import bs4
import requests
import sys
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.search = ""
        self.init_ui()

    def init_ui(self):

        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        self.add(grid)

        entry = Gtk.Entry()
        entry.connect("key-release-event", self.on_key_release)

        grid.attach(entry, 0, 0, 1, 1)
        button = Gtk.Button("Search")
        button.connect("clicked", self.destruct)
        grid.attach(button, 1, 0, 1, 1)

        self.set_border_width(2)
        self.set_title("Search Placement Blog")
        self.connect("destroy", Gtk.main_quit)

    def on_key_release(self, widget, event):
        self.search = widget.get_text()

    def destruct(self, widget):
        self.close()

def search_blog(soup, search):
    re = ''
    posts = soup.find_all('div', {'class':'post'})
    for post in posts:
        title = post.find('h2').text.lower()
        if search in title:
            re += str(post)

        if len(search.split()) > 1:
            s = [x[0] for x in search.split()]
            abb = ''
            for w in s:
                abb += w
            if abb in title:
                re += str(post)

    return re

if __name__ == "__main__":
    win = MyWindow()
    win.show_all()
    Gtk.main()

    search = win.search.lower()
    page_no = 1
    req = requests.get("http://170070011:Newlyf%400903@placements.iitb.ac.in/blog/?paged="+str(page_no))
    result = ""

    while req.status_code != 404:
        print("Searching Blog page %d ......" %page_no)
        soup = bs4.BeautifulSoup(req.content, "html.parser")
        result += search_blog(soup, search)

        page_no += 1
        req = requests.get("http://170070011:Newlyf%400903@placements.iitb.ac.in/blog/?paged="+str(page_no))


    f = open(os.path.expanduser('~/Desktop/index.html'), 'w')
    f.writelines(result)
    f.close()
    os.system("google-chrome ~/Desktop/index.html")