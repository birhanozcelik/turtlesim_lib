#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float64
from turtlesim.msg import Color
from turtlesim.srv import SetPen, Spawn
from geometry_msgs.msg import Twist
import time 

class Turtle:
    def __init__(self,name):
        rospy.init_node("turtlebot_controller")
        self.name = name
        self.twist_publisher = rospy.Publisher('/'+self.name+'/cmd_vel', Twist, queue_size=10)
        self.color_sensor = rospy.Publisher('/'+self.name+'/color_sensor', Color, queue_size=10)
        self.rate = rospy.Rate(20)
        self.color_service = rospy.ServiceProxy('/'+self.name+'/set_pen', SetPen)
        self.spawn_turtle = rospy.ServiceProxy('/spawn', Spawn)
        
        self.twist = Twist()
        self.twist.linear.x = 0.0
        self.twist.linear.y = 0.0
        self.twist.linear.z = 0.0
        self.twist.angular.x = 0.0
        self.twist.angular.y = 0.0
        self.twist.angular.z = 0.0

    def move(self,value):
        self.twist.linear.x = value
        self.twist_publisher.publish(self.twist)
    def rotate(self,value):
        self.twist.angular.z = value
        self.twist_publisher.publish(self.twist)
    def change_turtle(self,name):
        pass
    def change_pen(self,r,g,b,w,o):
        rospy.wait_for_service('/turtle1/set_pen')
        self.color_service(r,g,b,w,o)
    def spawn_turtle(self,x,y,theta,name):
        rospy.wait_for_service('/spawn')
        self.spawn_turtle(x,y,theta,name)
        
    def is_ok(self):
        if not rospy.is_shutdown():
            self.rate.sleep()
            return True
        else:
            return False

