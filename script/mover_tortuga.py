#!/usr/bin/env python3
# importacion de librerias de ros y tipo del mensaje
import  rospy
from geometry_msgs.msg import Twist
import sys

from rospy.exceptions import ROSInterruptException

def mover_tortuga(velocidad_lineal, velocidad_angular):
    rospy.init_node('mover_tortuga', anonymous=False)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)

    velocidad = Twist()

    while not rospy.is_shutdown():
        velocidad.linear.x = velocidad_lineal
        velocidad.linear.y = 0
        velocidad.linear.z = 0

        velocidad.angular.x = 0
        velocidad.angular.y = 0
        velocidad.angular.z = velocidad_angular

        rospy.loginfo("velocidad lineal = %f velocidad angular = %f ", velocidad_lineal,velocidad_angular)
        pub.publish(velocidad)

        rate.sleep()

if __name__ == '__main__':
    try:
        mover_tortuga(float(sys.argv[1]),float(sys.argv[2]))    

    except rospy.ROSInterruptException:
        pass

