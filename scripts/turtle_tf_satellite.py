#! /usr/bin/env python

import rospy
import tf
import math
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose



def handle_turtle_pose(msg):
	global counter
	br = tf.TransformBroadcaster()
	br.sendTransform((msg.x, msg.y, 0), quaternion_from_euler(0, 0, msg.theta), rospy.Time.now(), turtlename, "world")
	satellite = tf.TransformBroadcaster()
	satellite.sendTransform((math.sin(counter) * 1.5, math.cos(counter) * 1.5, 1), quaternion_from_euler(0, 0, counter), rospy.Time.now(), sat, "turtle1")
	counter += 0.01

	
if __name__ == '__main__':
	rospy.init_node('tf_tutrle')
	turtlename = rospy.get_param('~turtle_tf_name')
	sat = 'sat'
	counter = 0
		
	rospy.Subscriber('input_pose', Pose, handle_turtle_pose)
	rospy.spin()
