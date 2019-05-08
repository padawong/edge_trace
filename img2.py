import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("b2.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("b2_out.jpg",img)
