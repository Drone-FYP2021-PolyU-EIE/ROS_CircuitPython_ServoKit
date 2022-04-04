# ROS_CircuitPython_ServoKit
Simple ROS wripper for Adafruit_CircuitPython_ServoKit. We test it in Jetson NX and AGX. This should also work on pi 4 and other ciruitpython support platform
# topics
"/servo/angle", AllServoAngle       
# Prerequisites
* ROS
* Python3
* CircuitPython_ServoKit
# Install
[more install detail](https://github.com/Drone-FYP2021-PolyU-EIE/ServoKit/blob/master/README.md)
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
## AllServoAngle
Header + float32 array lenght of 16(0th mean channel 0, etc... )
```
rosmsg show ros_circuitpython_servokit_msgs/AllServoAngle
```
![image](https://user-images.githubusercontent.com/45313904/161604024-01f4141f-3401-474b-a498-2b43a42c7f23.png)

# Test i2c bus on Jetson
```bash
sudo i2cdetect -y -r <i2c bus>
```
# Common install problem on Jetson
## "Error:future feature annotations is not defined"
```bash
sudo -H pip3 install Adafruit-PlatformDetect==3.19.6
```
## "NameError: name 'I2C' is not defined"
```bash
sudo -H pip3 install adafruit-circuitpython-typing
```
