import cv2

image  = cv2.imread('D:/Python/Opencv/practice 1/flower.jpg')

horizontal = cv2.flip(image,0)
vertical = cv2.flip(image,1)
both = cv2.flip(image,-1)

cv2.imshow("Original",image)
cv2.imshow("horizontal",horizontal)
cv2.imshow("vertical",vertical)
cv2.imshow("both",both)

cv2.waitKey(0)
cv2.destroyAllWindows()

