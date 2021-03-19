#!/usr/bin/env python3

# created by Tanmay
#date 19 March 2021
from beginner_tutorials_tan.srv import AddTwoInt
from beginner_tutorials_tan.srv import AddTwoIntRequest
from beginner_tutorials_tan.srv import AddTwoIntResponse

import rospy

def handle(req):
    print("Returning [%s + %s = %s]"%(req.a,req.b,(req.a+req.b)))
    return AddTwoIntResponse(req.a + req.b)

def add_server():
    rospy.init_node("Add_two_int_server")
    s = rospy.Service('add_two_ints',AddTwoInt,handle)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
   add_server()
