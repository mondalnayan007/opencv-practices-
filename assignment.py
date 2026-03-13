import cv2

image = cv2.imread(input('Enter Your Image path :'))

gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

show_save = input("Show the image or save the image : ").lower()

if show_save == 'show':
    original_gray = input('Enter which type you want original/gary : ').lower()
    if original_gray == 'original':
        cv2.imshow("Image is showing" , image)
        cv2.waitKey()
        cv2.destroyAllWindows()
    elif original_gray == 'gray' :
        cv2.imshow("Image is showing" , gray)
        cv2.waitKey()
        cv2.destroyAllWindows()
    else :
        print('Invalid Choice')    

elif show_save == "save" :
     filename = input('Enter your new file name : ')
     cv2.imwrite(filename , gray)
    


else: 
    print("Invalid Command") 
