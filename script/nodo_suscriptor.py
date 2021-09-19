#!/usr/bin/env python3
# importacion de librerias
import rospy
from std_msgs.msg import String

# funcion llamada, la cual subscribimos al topic denominado "canal"

def llamada(data):
    rospy.loginfo(rospy.get_caller_id() + "Mensaje detecdado %s", data.data)


def nodo_suscriptor():
    rospy.init_node('nodo_suscriptor', anonymous=True)
    rospy.Subscriber('canal', String, llamada)
    rospy.spin()

if __name__ == '__main__':
    nodo_suscriptor()

