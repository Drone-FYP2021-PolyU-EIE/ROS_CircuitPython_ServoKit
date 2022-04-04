#!/usr/bin/env python3
from ast import If
import sys
# check pythone version
if sys.version_info < (3,0):
    print("Sorry, requires Python 3.x, not Python 2.x")
    sys.exit(1)

# i2c related
from adafruit_servokit import ServoKit
import board
import busio
import time

# ROS Related
import rospy
import message_filters # To Achieve Multiple subscriber
from ros_circuitpython_servokit_msgs.msg import AllServoAngle

class ros_circuitpython_servokit_node(object):
    def __init__(self):
        self.node_name = "servo_node"
        # Tells rospy the name of the node.
        # Anonymous = True makes sure the node has a unique name. Random
        # numbers are added to the end of the name.
        
        # Ros Node
        rospy.init_node("node_name", anonymous=True, disable_signals=True)
        self.loop_rate = rospy.Rate(1)

        # I2C
        rospy.loginfo("[%s]Initializing I2C BUS" % self.node_name)
        self.i2c_bus0=(busio.I2C(board.SCL, board.SDA))
        rospy.loginfo("[%s]Done Initializing PCA9685" % self.node_name)
        self.PCA9685 = ServoKit(channels=16, i2c=self.i2c_bus0)
        rospy.loginfo("[%s]Done initializing" % self.node_name)

        # ROS Topics
        self.servo_sub = message_filters.Subscriber("/servo/angle", AllServoAngle)
        self.servo_sub.registerCallback(self.callback_servo_input)

        self.servoValue = [0.0]*16


    def start(self):
        #keep the main loop running until
        while not rospy.is_shutdown():
            for i in range(16):
                self.PCA9685.servo[i].angle=self.servoValue[i]
                rospy.loginfo("[%s]%d:%f" % (self.node_name,i,self.servoValue[i]))

            self.loop_rate.sleep()

    
    def callback_servo_input(self,msg):
        self.servoValue= list(msg.all16servoPWM)
        #rospy.loginfo(self.servoValue[0])

if __name__ == '__main__':
    my_node = ros_circuitpython_servokit_node()
    my_node.start()
