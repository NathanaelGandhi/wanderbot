#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
	global g_range_ahead
	g_range_ahead = min(msg.ranges)

g_range_ahead = 1 # anything to start

scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('wander')
state_change_time = rospy.get_rostime()
driving_forward = True
rate = rospy.Rate(10)

while not rospy.is_shutdown():
	if driving_forward:
		print "driving forward. ahead: ", g_range_ahead
		if (g_range_ahead < 1.5 or rospy.get_rostime() > state_change_time):
			driving_forward = False
			state_change_time = rospy.get_rostime() + rospy.Duration(0.5)
	else: # we're not driving_forward
		print "not driving"
		if rospy.get_rostime() > state_change_time:
			driving_forward = True # we're done spinning, time to go forward
			state_change_time = rospy.get_rostime() + rospy.Duration(30)
	twist = Twist()
	if driving_forward:
		twist.linear.x = 1
	else:
		twist.angular.z = 1
	cmd_vel_pub.publish(twist)
	rate.sleep()