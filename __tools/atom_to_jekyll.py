#!/usr/bin/env python3

# A simple quick hack to convert an Atom feed to Jekyll blog posts
import feedparser
import re
import time

atom = feedparser.parse("https://feeds.launchpad.net/alarm-clock/announcements.atom")
for i in atom.entries:
    fname = time.strftime('%Y-%m-%d-', i.published_parsed) + re.sub("[^\\w\\.-]+", "", i.title.replace(" ", "-")) + ".html"
    author = i.authors[0]["name"]
    datestr = time.strftime('%Y-%m-%d %H:%M:%S %z', i.published_parsed)
    nl = "\n"
    headertitle = i.title.replace('"', '\\"')
    header = ("---\n"
            f'title:  "{headertitle}"{nl}'
            f'date:   {datestr}{nl}'
            f'author: "{author}"{nl}'
            "---\n")

    with open(fname, "w") as f:
        f.write(header)
        f.write(i.summary)
