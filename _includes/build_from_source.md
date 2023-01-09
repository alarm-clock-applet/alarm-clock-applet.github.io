## Building and Installing
Download and extract the source code with:
```
wget --content-disposition https://github.com/alarm-clock-applet/alarm-clock/archive/refs/tags/<VERSION>.tar.gz
tar zxvf alarm-clock-<VERSION>.tar.gz
cd alarm-clock-<VERSION>
```

And compile - install with the usual:
```
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make
sudo make install
```
