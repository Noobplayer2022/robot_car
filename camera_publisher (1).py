#!/usr/bin/env python3


import rospy
# send messages from of images
from sensor_msgs.msg import Image

#cv_bridge is package tha has library for converting openCV image into ros message image  
from cv_bridge import CvBridge

import cv2

publisherNodeName='camera_sensor_publisher'

topicName='video_topic'

# init the node
rospy.init_node(publisherNodeName,anonymous=True)

# buffer size is queue
publisher=rospy.Publisher(topicName,Image, queue_size=60)

rate = rospy.Rate(60)

videoCaptureObject=cv2.VideoCapture(0)

bridgeObject=CvBridge()

while not rospy.is_shutdown():

    returnValue, capturedFrame = videoCaptureObject.read()

    if returnValue == True:
        rospy.loginfo('video frame captured and published')

        imageToTransmit = bridgeObject.cv2_to_imgmsg(capturedFrame)

        publisher.publish(imageToTransmit)

    rospy.sleep(0.75)