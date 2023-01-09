---
title:  "Alarm Clock 0.4.1 \"Happy New Year\" released!"
date:   2023-01-09 05:13:01 
author: "Tasos Sahanidis"
---
#### [GitHub Release](https://github.com/alarm-clock-applet/alarm-clock/releases/tag/alarm-clock-applet-0.4.1)
This release fixes numerous issues and removes all legacy dependencies. The minimum supported Ubuntu version is now 18.04.

### Major Changes:
* The application has been ported to GTK 3, and will thus look slightly different.
* Old GTK Tray Icon support has been removed. A desktop environment with support for AppIndicators/StatusNotifierItem is required.
* Alarms have been migrated to GSettings.

### Notable Fixes:
* Many memory leaks (including a massive one while the UI was visible)
* Alarm labels bouncing horizontally every second
* Debug messages breaking alarms and timers
* Compile errors

### New Features:
* Default media players are now autodetected.
* More media players can be controlled using playerctl out of the box.
* More system sounds are now added to the list by default.

### Full Changelog:
[0.3.4...0.4.1](https://github.com/alarm-clock-applet/alarm-clock/compare/0.3.4...0.4.1)

### Notes for package maintainers:
Many dependencies have changed and the project is now built with CMake. If available, please build with GConf2 support enabled so that people can migrate any old alarms they might have, even if they built from source previously. If possible, also add `playerctl` as an optional/recommended dependency; its presence is detected at runtime.

### What happened to 0.4.0?
It was meant to be tagged right before the major rewrite/porting work started, however it was tagged at the wrong commit by accident, and is thus now ignored.