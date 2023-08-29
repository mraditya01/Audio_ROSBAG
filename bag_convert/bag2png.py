import subprocess
import rosbag
import cv2
from cv_bridge import CvBridge
import numpy as np

BAGFILE = "/home/radit/Data/2023-06-24-13-09-54_544.bag"

if __name__ == '__main__':
    bag = rosbag.Bag(BAGFILE)
    for i in range(5):
        TOPIC = f'/ladybug/camera{i}/image_raw'
        DESCRIPTION = 'depth_'
        image_topic = bag.read_messages(TOPIC)
        for k, b in enumerate(image_topic):
            bridge = CvBridge()
            cv_image = bridge.imgmsg_to_cv2(b.message, b.message.encoding)
            cv_image.astype(np.uint8)
            cv2.imwrite('/home/radit/test/' + str(i) + str(b.timestamp) + '.png', cv_image)
            print('saved: ' '/home/radit/test/' + str(i) + str(b.timestamp) + '.png')


    bag.close()

    print('PROCESS COMPLETE')