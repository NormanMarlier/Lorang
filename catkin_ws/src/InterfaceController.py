#!/usr/bin/env python

"""

docstring

"""

# Import module
import rospy
from std_msgs.msg import Empty


# Meta data
__author__ = 'Norman Marlier'
__copyright__ = 'Copyright 2018'
__credits__ = ['Norman Marlier']
__maintainer__ = "Norman Marlier"
__email__ = "norman.marlier@student.uliege.be"
__status__ = "Prototype"


def talker():
    Empty msg;
    pub = rospy.Publisher('lorang', Empty, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo('Change the state of the gripper')
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



