#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def rrbotmove():
    rospy.init_node('rrbot_pub', anonymous=True)
    pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
    rate=rospy.Rate(5)

    while not rospy.is_shutdown():
        joint1 = 1.57

        pub1.publish(joint1)
        pub2.publish(joint1)
        rate.sleep()

if __name__ == '__main__':  
    try:
        rrbotmove() 
    except rospy.ROSInterruptException:
        pass

