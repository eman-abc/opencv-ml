import cv2

image_paths = [
    'street.jpg', 'cars.jpg',  'kitten.jpg', 'circuit.jpg']

blue = [255, 0, 0]
orange = [0, 165, 255]  
red = [0, 0, 255]
black = [0, 0, 0]


def resize_for_display(image, max_width=800, max_height=600):
    h, w = image.shape[:2]
    scale_w = max_width / w
    scale_h = max_height / h
    scale = min(scale_w, scale_h)
    new_size = (int(w * scale), int(h * scale))
    return cv2.resize(image, new_size)

for image_path in image_paths:
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: The image '{image_path}' can't load")
        continue
    modified_img = img.copy()

    height, width = modified_img.shape[:2]
    print(f"Image '{image_path}' loaded with dimensions: {width}x{height}")

    # get the center 
    cx, cy = width // 2, height // 2

    # diagonal blue line
    cv2.line(modified_img, (0, 0), (width - 1, height - 1), blue, thickness=4)

    # rd rectangle centered
    rect_w, rect_h = width // 4, height // 4
    start_point = (cx - rect_w // 2, cy - rect_h // 2)
    end_point = (cx + rect_w // 2, cy + rect_h // 2)
    cv2.rectangle(modified_img, start_point, end_point, red, thickness=4)

    # black circle concentric w rect
    radius = min(rect_w, rect_h) // 2
    cv2.circle(modified_img, (cx, cy), radius, black, thickness=6)

    # orange text bottom left
    text = "Sundas Eman"
    text_position = (int(width * 0.05), int(height * 0.95))
    cv2.putText(modified_img, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 5, orange, thickness=6)

    
    # displau the resized image
    display_img = resize_for_display(modified_img)
    cv2.imshow(f"Modified {image_path}", display_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
