#!/usr/bin/env bash

# Download/Update JSON resources
DATADIR="_data/"
if [[ ! -d "$DATADIR" ]]; then
    echo "Please run this script at the root of the repository ($DATADIR not found)"
    exit 1
fi
wget -O "${DATADIR}tags.json" https://api.github.com/repos/alarm-clock-applet/alarm-clock/tags
wget -O "${DATADIR}releases.json" https://api.github.com/repos/alarm-clock-applet/alarm-clock/releases
