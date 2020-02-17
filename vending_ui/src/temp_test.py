# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
import random

rospy.init_node('temp_test', anonymous=True)

r = rospy.Rate(10)
temp_msg = Float32()

temp_pub = rospy.Publisher('drink_temp', Float32, queue_size=5)

while not rospy.is_shutdown():
    temp_msg.data = random.uniform(10, 30)
    print temp_msg.data
    temp_pub.publish(temp_msg)
    r.sleep()
