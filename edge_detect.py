# Input format: python edge_detect.py --input hand_drawn_test/back_pen_flash.jpg
# If getting an imread error, first double-check correctness of file path 

import cv2
import numpy as np
import argparse
import os # Library will be used to take input and split the path

from matplotlib import pyplot as plt

parser = argparse.ArgumentParser(description='Edge detection')
parser.add_argument('--input', help='input file')
args = parser.parse_args()
print(args.input)

img = cv2.cv2.imread(args.input, 1)
    
# Take each frame
#_, frame = .read()

#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])
                            
mask = cv2.inRange(img, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask= mask)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

# os.path automatically searches for the appropriate path marker, in this case '/'
head, tail = os.path.split(args.input)
print(head)
print(tail)

cv2.imwrite(os.path.join(head,'Original_' + tail), img)
cv2.imwrite(os.path.join(head,'Mask_' + tail), mask)
cv2.imwrite(os.path.join(head,'Laplacian_' + tail), laplacian)
cv2.imwrite(os.path.join(head,'Sobelx_' + tail), sobelx)
cv2.imwrite(os.path.join(head,'Sobely_' + tail), sobely)

cv2.destroyAllWindows()
