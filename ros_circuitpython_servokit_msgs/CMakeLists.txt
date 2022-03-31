cmake_minimum_required(VERSION 2.8.3)
project(ros_circuitpython_servokit_msgs)

find_package(catkin REQUIRED COMPONENTS message_generation std_msgs)

#include_directories(include)

add_message_files(
  DIRECTORY msg
  FILES
  AllServoAngle.msg
)

#add_service_files(
#
#)

# add_action_files(
#   DIRECTORY action
#   FILES
#   Action1.action
#   Action2.action
# )

generate_messages(DEPENDENCIES std_msgs)

catkin_package(
  # INCLUDE_DIRS include
  CATKIN_DEPENDS message_runtime std_msgs)