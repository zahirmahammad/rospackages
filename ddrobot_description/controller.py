#!/usr/bin/python3
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from numpy import arctan2
import time
from std_msgs.msg import Float64
import math


x = 0
y = 0
theta = 0


def talker():
    pub1 = rospy.Publisher('/ddrobot/Rev4_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/ddrobot/Rev5_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/ddrobot/Rev6_position_controller/command', Float64, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    for i in range(2):
        # hello_str = "hello world %s" % rospy.get_time()
        position=math.pi
        pub2.publish(position/7)
        time.sleep(1)
        pub3.publish(position/3)
        time.sleep(1)
        rate.sleep()

    val=position*0.25
    for i in range(10):
        pub2.publish(position/2.5)
        time.sleep(0.5)
        # rospy.loginfo(position)
        pub2.publish(position/7)
        time.sleep(0.5)
        pub1.publish(val)
        time.sleep(0.5)
        val=val+(position*0.25)
        if val>6.5:
            val=position*0.25
    
    time.sleep(2)
    pub3.publish(0)
    time.sleep(1)
    pub2.publish(0)
    time.sleep(1)
    pub1.publish(0)



def newOdom(msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

rospy.init_node("ddrobot_path")
sub = rospy.Subscriber("odom", Odometry, newOdom)
pub = rospy.Publisher("cmd_vel", Twist, queue_size = 1)

speed = Twist()
r=rospy.Rate(4)

def move_forward(n):
    speed.linear.x=1.0
    for i in range(n):
        pub.publish(speed)
        r.sleep()
    speed.linear.x=0.0
    pub.publish(speed)

def turn_left():
    speed.angular.z=1.0
    for i in range(7):
        pub.publish(speed)
        r.sleep()
    speed.angular.z=0.0
    pub.publish(speed)

def turn_right():
    speed.angular.z=-1.0
    for i in range(7):
        pub.publish(speed)
        r.sleep()
    speed.angular.z=0.0
    pub.publish(speed)







move_forward(10)
turn_left()
move_forward(10)
turn_left()
move_forward(10)
turn_right()
print("Initiailzing Robotic arm")
try:
    talker()
except rospy.ROSInterruptException:
    pass
