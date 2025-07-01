import cv2

img_path = ['street.jpg', 'cars.jpg', 'kitten.jpg', 'circuit.jpg']

for image in img_path:
    img = cv2.imread(image)
    if img is None:
        print(f"Error: The image '{image}' cant load")
    else:
        height, width = img.shape[:2]
        print(f"Image '{image}' loaded with dimensions: {width}x{height}")
        print(f"img.shape: {img.shape}")
        mid_y, mid_x = height // 2, width // 2

        # croppinggg
        top_left = img[0:mid_y, 0:mid_x]
        top_right = img[0:mid_y, mid_x:width]
        bottom_left = img[mid_y:height, 0:mid_x]
        bottom_right = img[mid_y:height, mid_x:width]

        cv2.imshow(f"{img_path} - Top Left", top_left)
        cv2.imshow(f"{img_path} - Top Right", top_right)
        cv2.imshow(f"{img_path} - Bottom Left", bottom_left)
        cv2.imshow(f"{img_path} - Bottom Right", bottom_right)

        print(f"Quadrants of: {img_path}")
        cv2.waitKey(0)
        cv2.destroyAllWindows()