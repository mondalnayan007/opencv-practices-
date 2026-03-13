import cv2 

image  = cv2.imread('D:\Python\Opencv\practice 1\opencv.png')

if image is not None:
    success = cv2.imwrite("updated.png" , image)
    if success : 
        print("Image Saved Successful")
    else:
        print("Image is not saved")

else:
    print("Please Load an image first")
