#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


if __name__ == '__main__':
    # Initializing a node which will work as the publisher node
     rospy.init_node('publisher_node', anonymous=True)

    # Generating a publisher for the topic "Speaker"
     pub = rospy.Publisher("Speaker", String, queue_size=10)

    # Message publishing rate is set to 1 Hz 
     rate = rospy.Rate(1.0)
    

    # Loop will continue until the node is shutdown manually
     while not rospy.is_shutdown():
        # Creating a message object
          msg = String()
          msg.data = "Hello Project Altair! [sent from the publisher node]"
      
        # Publishing the message
          pub.publish(msg)

          rate.sleep()
   