import cv2

image  = cv2.imread('D:/Python/Opencv/practice 1/flower.jpg')


if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Black & White image is showing" , gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    success = cv2.imwrite("flower_grayscale.png" , gray)
else:
    print("Could note load image")