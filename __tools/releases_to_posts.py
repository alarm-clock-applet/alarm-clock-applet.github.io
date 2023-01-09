#!/usr/bin/env python3
import json
import datetime
import pathlib
import sys
import re

authors = {
    "tatokis": "Tasos Sahanidis",
}

with open("_data/releases.json") as jf:
    jrel = json.load(jf)
    processed = 0
    for rel in jrel:
        if rel["draft"] or rel["prerelease"]:
            continue

        title = rel["name"] + " released!"
        date = datetime.datetime.strptime(rel["published_at"], "%Y-%m-%dT%H:%M:%SZ")

        fpath = pathlib.Path("_posts", date.strftime('%Y-%m-%d-') + re.sub("[^\\w\\.-]+", "", title.replace(" ", "-")) + ".md")
        if fpath.exists():
            print(f"{fpath} already exists.")
            continue

        processed += 1

        author = authors[rel["author"]["login"]] if rel["author"]["login"] in authors else rel["author"]["login"]
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
            mdf.write(f"#### [GitHub Release]({rel['html_url']}){nl}")
            mdf.write(rel["body"])

    if processed == 0:
        print("No posts have been processed. Have you ran __tools/update_data.sh ?")
        sys.exit(1)
