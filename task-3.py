import cv2

image_path = [
    'street.jpg', 'cars.jpg', 'kitten.jpg', 'circuit.jpg']

for image in image_path:
    img = cv2.imread(image)
    if img is None:
        print(f"Error: The image '{image}' cant load")
    else:
        modified_img = img.copy()
        height, width = img.shape[:2]
        print(f"Image '{image}' loaded with dimensions: {width}x{height}")

        blue=[255, 0, 0]
        orange=[0, 165, 255]

        for y in range(0, width, 4):
            if y < width:
                modified_img[:, y] = blue
            if y+2 < width:
                modified_img[:, y+2] = orange


        cv2.imshow(f"Modified {image}", modified_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()