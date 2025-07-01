import cv2
import os
import numpy as np

image_paths = ['street.jpg', 'cars.jpg', 'kitten.jpg', 'circuit.jpg']

for image_path in image_paths:

    imag = cv2.imread(image_path)
    if imag is None:
        print(f"Error: Could not load '{image_path}'")
        continue

    height, width = imag.shape[:2]
    print(f"Image '{image_path}' loaded with dimensions: {width}x{height}")
    
    img = imag.copy()
    name = os.path.splitext(image_path)[0]  

    # resize
    img1 = cv2.resize(img, (int(width / 2), int(height / 2)))
    img2 = cv2.resize(img, (int(width * 3 / 4), int(height / 2))) #switch up aspect ration
    img3 = cv2.resize(img, (int(width / 3), int(height / 3)))

    cv2.imwrite(f'resized_{name}_1.jpg', img1)
    cv2.imwrite(f'resized_{name}_2.jpg', img2)
    cv2.imwrite(f'resized_{name}_3.jpg', img3)


    # 4 images at once
    cv2.imshow(f"{name} - Original", img)
    cv2.imshow(f"{name} - Resized 1 (1/2)", img1)
    cv2.imshow(f"{name} - Resized 2 (3/4 x 1/2)", img2)
    cv2.imshow(f"{name} - Resized 3 (1/3)", img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

