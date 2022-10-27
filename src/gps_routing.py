#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import NavSatFix

def gps_callback(data):
	rospy.loginfo("GPS Lat Lon Alt: ", data.latitude, data.longitude, data.altitude)

if __name__ == '__main__':
	rospy.init_node('message_router_server')
	rate = rospy.Rate(10)

	rospy.Subscriber("/drone1_gps", NavSatFix, gps_callback)

	rospy.spin()