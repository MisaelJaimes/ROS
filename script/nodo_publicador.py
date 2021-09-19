#!/usr/bin/env python3
# importacion de librerias 
import rospy
from std_msgs.msg import String

def publicador():
    # creamos el objeto publicador ingresando el nombre del topic, el tipo de dato y el numero
    # de datos en cola permitido en el topic
    pub = rospy.Publisher('canal', String, queue_size=10)
    # inciamos el nodo
    rospy.init_node('nodo_publicador', anonymous=True)
    # definimos la velocidad de cilcos por segundo
    rate = rospy.Rate(10) # 10hz
    # cramos un ciclo para determinar si no se ha ejecutado un comando de salida como control + c
    while not rospy.is_shutdown():
        informacion = "HOLA USUARIO %s" % rospy.get_time()
        rospy.loginfo(informacion)
        pub.publish(informacion)
        rate.sleep()

if __name__ == '__main__':
    try:
        publicador()
    # deteccion de interrupcion externa en el nodo oacionada por ROS
    except rospy.ROSInterruptException:
        pass