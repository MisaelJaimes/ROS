#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from rospy.exceptions import ROSInterruptException
mensaje = Twist()

def llamada(data):
    rospy.loginfo(data.linear.x)
    rospy.loginfo(data.linear.y)
    rospy.loginfo(data.linear.z)
    mensaje = data
    mover_tortuga(mensaje)

def teleopTurtle():
    rospy.init_node('teleopTurtle', anonymous = True)
    rospy.Subscriber("/cmd_vel", Twist, llamada)
    rospy.spin()

def mover_tortuga(mensaje):
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size= 10)
    rate = rospy.Rate(10)
    pub.publish(mensaje)


if __name__ == "__main__":
    try:
        teleopTurtle()
    except rospy.ROSInterruptException:
        pass