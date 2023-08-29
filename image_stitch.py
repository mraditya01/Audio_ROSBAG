# import stitching
# import cv2

# stitcher = stitching.Stitcher()
# panorama = stitcher.stitch([f"1/frame0000.jpg", f"2/frame0000.jpg", f"3/frame0000.jpg", f"4/frame0000.jpg", f"5/frame0000.jpg"])

# cv2.imwrite("test.jpg",

# from imutils import paths
import numpy as np
import argparse
import cv2

imagePaths = [f"1/frame0000.jpg", f"2/frame0000.jpg", f"3/frame0000.jpg", f"4/frame0000.jpg", f"5/frame0000.jpg"]
images = []

for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	images.append(image)

# initialize OpenCV's image stitcher object and then perform the image
# stitching
print("[INFO] stitching images...")
stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

# if the status is '0', then OpenCV successfully performed image
# stitching
if status == 0:
	# write the output stitched image to disk
	cv2.imwrite('test2.jpg', stitched)
	# display the output stitched image to our screen
	cv2.imshow("Stitched", stitched)
	cv2.waitKey(0)
# otherwise the stitching failed, likely due to not enough keypoints)
# being detected
else:
	print("[INFO] image stitching failed ({})".format(status))