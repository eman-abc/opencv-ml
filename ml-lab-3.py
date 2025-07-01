import cv2

img1 = cv2.imread('street.jpg')  # Ensure the image file names are correct
img2 = cv2.imread('cars.jpg')       
img3 = cv2.imread('kitten.jpg')
img4 = cv2.imread('circuit.jpg')

if img1 is None or img2 is None or img3 is None or img4 is None:
    print("Error: One or more images could not be loaded.")     
else:
    #  resizable windows
    cv2.namedWindow('Street', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Cars', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Kitten', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Circuit', cv2.WINDOW_NORMAL)

    cv2.imshow('Street', img1)
    cv2.imshow('Cars', img2)          
    cv2.imshow('Kitten', img3)
    cv2.imshow('Circuit', img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
