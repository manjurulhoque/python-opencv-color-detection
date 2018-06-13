import sys
import numpy as np
import cv2

blue = sys.argv[1]
green = sys.argv[2]
red = sys.argv[3]

color = np.uint8([[[blue, green, red]]])
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)  # converting BGR to HSV

hue = hsv_color[0][0][0]  # Getting hue value

print("Lower bound is :"),
print("[" + str(hue - 10) + ", 100, 100]\n")  # lower bound

print("Upper bound is :"),
print("[" + str(hue + 10) + ", 255, 255]")  # upper bound

img = cv2.imread('circles.png', 1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([hue - 10, 100, 100], dtype=np.uint8)
upper_range = np.array([hue + 10, 255, 255], dtype=np.uint8)

mask = cv2.inRange(hsv, lower_range, upper_range)
output = cv2.bitwise_and(img, img, mask=mask)

# cv2.imshow('mask', hsv_color)
# cv2.imshow('image', output)
cv2.imshow("images", np.hstack([img, output]))

while True:
    k = cv2.waitKey(0)
    if k == 27:
        break

cv2.destroyAllWindows()
