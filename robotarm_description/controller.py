#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random
import time

def talker():
    pub1 = rospy.Publisher('/robotarm/Rev4_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/robotarm/Rev5_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/robotarm/Rev6_position_controller/command', Float64, queue_size=10)
    rospy.init_node('armrobot_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        position=2.0
        pub3.publish(position)
        rospy.loginfo(position)

        time.sleep(1)
        pub3.publish(-position)
        rospy.loginfo(-position)

        time.sleep(1)
        rate.sleep()

        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
       pass 
