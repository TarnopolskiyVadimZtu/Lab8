import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Tarnopolskiy.jpg")
# DISPLAY
cv2.imshow("Frame", img)
cv2.waitKey(0)
