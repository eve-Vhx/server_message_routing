#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix
import numpy as np

def gps_callback(data):
	rospy.loginfo("GPS Lat Lon Alt: ", data.latitude, data.longitude, data.altitude)

	gps_data = np.array([data.latitude, data.longitude, data.altitude])
	with open('../../gps_data.csv', 'w', newline='') as file:
	    mywriter = csv.writer(file, delimiter=',')
	    mywriter.writerow(gps_data)

if __name__ == '__main__':
	rospy.init_node('message_router_server')
	rate = rospy.Rate(10)

	rospy.loginfo("Running the node...")

	rospy.Subscriber("/drone1_gps", NavSatFix, gps_callback)

	rospy.spin()