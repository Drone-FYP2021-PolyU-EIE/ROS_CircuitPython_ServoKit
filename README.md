# ROS_CircuitPython_ServoKit
Simple ROS wripper for Adafruit_CircuitPython_ServoKit. We test it in Jetson NX and AGX. This should also work on pi 4 and other ciruitpython support platform 
# Prerequisites
* ROS
* Python3
* CircuitPython_ServoKit
# Install
```bash
git clone https://github.com/Drone-FYP2021-PolyU-EIE/ServoKit.git
cd ServoKit
bash installServoKit.sh
```
Now cd to your catkin workspace/src   
```bash
git clone https://github.com/Drone-FYP2021-PolyU-EIE/ROS_CircuitPython_ServoKit.git
catkin_make --cmake-args \
      -DPYTHON_EXECUTABLE=/usr/bin/python3
```      
# Custom ROS Message

# test jetson
```bash
sudo i2cdetect -y -r <i2c bus>
```
