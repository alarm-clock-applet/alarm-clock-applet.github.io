#!/usr/bin/env bash

# Download/Update JSON resources
DATADIR="_data/"
if [[ ! -d "$DATADIR" ]]; then
    echo "Please run this script at the root of the repository ($DATADIR not found)"
    exit 1
fi
wget -O "${DATADIR}tags.json" https://api.github.com/repos/alarm-clock-applet/alarm-clock/tags
wget -O "${DATADIR}releases.json" https://api.github.com/repos/alarm-clock-applet/alarm-clock/releases

README=$(wget -O - https://raw.githubusercontent.com/alarm-clock-applet/alarm-clock/master/README.md)

echo "$README" | python3 -c 'import sys; s = sys.stdin.read(); print(s.split("<!-- requirements_ubuntu -->")[-1].split("<!-- end requirements_ubuntu -->")[0].strip())' > _includes/requirements_ubuntu.md
echo "$README" | python3 -c 'import sys; s = sys.stdin.read(); print(s.split("<!-- build_from_source -->")[-1].split("<!-- end build_from_source -->")[0].strip())' > _includes/build_from_source.md
