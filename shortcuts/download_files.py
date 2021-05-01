import os
import bs4
import sys

with open(sys.argv[1], 'r') as f:
    webpage = f.read()

soup = bs4.BeautifulSoup(webpage, "html.parser")
a = soup.find_all("a", {"class": "file"})
d = os.listdir(".")

failed = []

for i, link in enumerate(a):
    print("----------- Downloading %d of %d ----------------" % (i+1, len(a)))
    if str(link.contents[1]) in d:
        continue
    r = os.system("wget " + link.attrs['href'])
    if r:
        print(link)
        failed.append(link)

print failed
