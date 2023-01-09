## Building and Installing
Extract the source code with:
```
tar zxvf alarm-clock-applet-<VERSION>.tar.gz
cd alarm-clock-applet-<VERSION>
```

And compile - install with the usual:
```
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make
sudo make install
```
