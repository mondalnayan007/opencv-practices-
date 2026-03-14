import cv2 

image = cv2.imread('D:\Python\Opencv\practice 1\strawberry.jpg')

croped_image = image[100:500 , 300:1500]
cv2.imshow("Original",image)
cv2.imshow("Cropped Image is showing" ,  croped_image)
cv2.waitKey()
cv2.destroyAllWindows()