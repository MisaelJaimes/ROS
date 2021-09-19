#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from rospy.exceptions import ROSInterruptException
data = Twist()

def llamada(data):
    rospy.loginfo(data.linear.x)
    rospy.loginfo(data.linear.y)
    rospy.loginfo(data.linear.z)
    

def teleopTurtle():
    rospy.init_node('teleopTurtle', anonymous = True)
    rospy.Subscriber("/cmd_vel", Twist, llamada)
    rospy.spin()


if __name__ == "__main__":
    try:
        teleopTurtle()
    except rospy.ROSInterruptException:
        pass