#!/usr/bin/env python
# The above line is to make the python script a stand-alone executable
import rospy 
from std_msgs.msg import String 
def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10) # Creating an instance of a publisher using this function, where chatter is the name of the topic, having data type String
	rospy.init_node('talker', anonymous=True) # using this function to tell ROS that this python script will be a node
	rate = rospy.Rate(10) # rate of loopping is 10Hz (kept constant)
	while not rospy.is_shutdown():
		hello_str = "hello world %s" % rospy.get_time() # text will be published followed by the time 
		pub.publish(hello_str) 
		rate.sleep()		# it will keep rate of publishing constant

if __name__=='__main__': 
	try:
		talker()	# function call
	except rospy.ROSInterruptException:
		pass 
