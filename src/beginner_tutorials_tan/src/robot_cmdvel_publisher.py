#!/usr/bin/env python3
#subscriber to the pose of the turtlesim robot

# created by Tanmay
# date 19 March 2020


import rospy
from geometry_msgs.msg import Twist

# def callback(message):
#     rospy.loginfo(rospy.get_caller_id() + " x = %s y = %s theta = %s linear_v = %s angular_v = %s",message.x,message.y,message.theta,message.linear_velocity,message.angular_velocity)


# def subscribe():

#     rospy.init_node("POSE",anonymous=True)
    
#     rospy.Subscriber("/turtle1/cmd_vel",String,callback)


# if __name__ == '__main__':
#     try:
#         listener()
#     except e=rospy.exceptions():
#         rospy.loginfo("Erro occurred %s",e)

def talker():
    speed_pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    rospy.init_node("talker",anonymous=True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 2.0
        twist.linear.y = 0.0
        twist.angular.z = 2.0
        rospy.loginfo("Publishing")
        speed_pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException as e:
        rospy.loginfo("(TAN) Error: %s",e)