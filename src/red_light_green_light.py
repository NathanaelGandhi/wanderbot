#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

#print "Starting package"
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('red_light_green_light')

red_light_twist = Twist()
green_light_twist = Twist()
green_light_twist.linear.x = 0.5

driving_forward = False
light_change_time = rospy.get_rostime()
rate  = rospy.Rate(10)

while not rospy.is_shutdown():
#	print light_change_time
#	print rospy.get_rostime()
	if driving_forward:
#		print "pub green light"
		cmd_vel_pub.publish(green_light_twist)
	else:
#		print "pub red light"
		cmd_vel_pub.publish(red_light_twist)
	if light_change_time < rospy.get_rostime():
		print "flipping driing_forward"
		driving_forward = not driving_forward
		light_change_time = rospy.get_rostime() + rospy.Duration(3)
	rate.sleep()
