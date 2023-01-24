#!/usr/bin/env python3
import json
import datetime
import pathlib
import sys
import re
import urllib.request
import common

url = "https://api.github.com/repos/alarm-clock-applet/alarm-clock/issues?labels=announcement"
announcements_str = urllib.request.urlopen(url).read()
announcements = json.loads(announcements_str)

processed = 0
for ann in announcements:
    if ann["author_association"] != "MEMBER":
        continue

    title = re.sub("^announcement:? ?", "", ann["title"], flags=re.IGNORECASE)
    date = datetime.datetime.strptime(ann["created_at"], "%Y-%m-%dT%H:%M:%SZ")

    fpath = pathlib.Path("_posts", date.strftime('%Y-%m-%d-') + re.sub("[^\\w\\.-]+", "", title.replace(" ", "-")) + ".md")
    if fpath.exists():
        print(f"{fpath} already exists.")
        continue

    processed += 1

    author = common.authors[ann["user"]["login"]] if ann["user"]["login"] in common.authors else ann["user"]["login"]
    datestr = date.strftime('%Y-%m-%d %H:%M:%S %z')

    nl = "\n"
    headertitle = title.replace('"', '\\"')
    headerauthor = author.replace('"', '\\"')
    header = ("---\n"
        f'title:  "{headertitle}"{nl}'
        f'date:   {datestr}{nl}'
        f'author: "{headerauthor}"{nl}'
        "---\n")

    with open(fpath, "w") as mdf:
        mdf.write(header)
        mdf.write(ann["body"])

if processed == 0:
    print("No new announcements found.")
