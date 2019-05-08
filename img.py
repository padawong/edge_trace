import cv2
import numpy as np

img = cv2.cv2.imread('test.jpg', 1)
from matplotlib import pyplot as plt
    
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

cv2.imwrite('test_Original.jpg',img)
cv2.imwrite('test_Mask.jpg',mask)
cv2.imwrite('test_laplacian.jpg',laplacian)
cv2.imwrite('test_sobelx.jpg',sobelx)
cv2.imwrite('test_sobely.jpg',sobely)

cv2.destroyAllWindows()
