import cv2 

image = cv2.imread('D:\Python\Opencv\practice 1\opencv.png')

cv2.imshow("Before Resize" , image)



resized = cv2.resize(image , (100,100))

cv2.imshow("After resize" , resized)
cv2.waitKey()
cv2.destroyAllWindows()