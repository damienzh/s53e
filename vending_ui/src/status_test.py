#! /usr/bin/env python

import rospy
from std_msgs.msg import String
import random

rospy.init_node('status_test', anonymous=True)

status_pub = rospy.Publisher('drink_stats', String, queue_size=5)

rate = rospy.Rate(1)

while not rospy.is_shutdown():
    vacant = random.randint(0, 5)
    s = list('111111')
    s[vacant] = '0'
    status_pub.publish(''.join(s))
    rate.sleep()
