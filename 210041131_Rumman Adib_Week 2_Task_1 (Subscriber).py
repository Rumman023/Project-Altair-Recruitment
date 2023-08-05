#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Received message [@ subscriber node]: %s", msg.data)


if __name__ == '__main__':
    # Initializing a node which will work as the subscriber node
    rospy.init_node('subscriber_node', anonymous=True)

    # Generating a subscriber for the topic "Speaker"
    rospy.Subscriber('Speaker', String, callback)

    # keeping the node alive until it is shut down manually
    rospy.spin()
