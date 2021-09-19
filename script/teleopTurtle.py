import rospy
from geometry_msgs import Twist

def llamada():
    rospy.loginfo("Informacion resivida: %s", data.data)

def teleopTurtle():
    rospy.init_node('teleopTurtle', anonymous = True)
    rospy.Subscriber("/cmd_vel", Twist, llamada)
    rospy.spin()


if __name__ == "__main__":
    try:
        teleopTurtle()
    except rospy.ROSInterruptException:
        pass