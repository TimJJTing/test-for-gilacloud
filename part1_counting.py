# part1_counting.py
# Given a list of urls, print out the top 3 frequent filenames.
# e.g.
urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]
# The program should print out
# a.txt 3
# b.txt 2
# c.jpg 2

import re
pattern = r'.*\/(?P<name>[0-9A-Za-z\.\-_]*\.\w*?)$'
files = {}

for url in urls:
    filename = re.match(pattern, url).group("name")
    if filename not in files:
        files[filename] = 1
    else:
        files[filename] += 1

for item in sorted(files.items(), key=lambda obj: obj[1], reverse=True)[:3]:
    print("%s %s"%(item[0], item[1]))
