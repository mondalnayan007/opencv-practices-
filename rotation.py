import cv2 

image = cv2.imread("D:\Python\Opencv\practice 1\opencv.png")

h,w = image.shape[:2]

center = (h//2 , w//2)

M = cv2.getRotationMatrix2D(center , 60, 0.5)

rotated_image= cv2.warpAffine(image,M,(w,h))

cv2.imshow("Before Rotation" , image)

cv2.imshow("After rotation" , rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()