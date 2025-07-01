import cv2

image_paths = ['street.jpg', 'cars.jpg', 'kitten.jpg', 'circuit.jpg']


colors = [
    (255, 0, 0),    # Blue
    (0, 255, 0),    # Green
    (0, 0, 255),    # Red
    (0, 255, 255)   # Yellow
]

square_size = 50  
gap_size = 25    # space between squares

for image_path in image_paths:
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Could not load '{image_path}'")
        continue

    height, width = img.shape[:2]
    modified_img = img.copy()

    for y in range(0, height, square_size + gap_size):
        for x in range(0, width, square_size + gap_size):
            #  color picked based on position
            color_index = ((x // (square_size + gap_size)) + (y // (square_size + gap_size))) % len(colors)
            color = colors[color_index]

            #  square coordinates 
            top_left = (x, y)
            bottom_right = (
                min(x + square_size, width),
                min(y + square_size, height)
            )

            # draw filled square
            cv2.rectangle(modified_img, top_left, bottom_right, color, thickness=-1)

    cv2.imshow(f"Squares with Gaps - {image_path}", modified_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

