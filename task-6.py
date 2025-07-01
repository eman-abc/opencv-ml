import cv2
import random


image_path = 'cars.jpg'
img = cv2.imread(image_path)
if img is None:
    print(f"Error loading image '{image_path}'")
    exit()

# clone original image for drawing
img_copy = img.copy()
boxes = []  # store bounding boxes
drawing = False
start_point = (-1, -1)

#  list of random distinct colors
def get_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

colors = []

# mouuse callback function
def draw_rectangle(event, x, y, flags, param):
    global start_point, drawing, img_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()
            cv2.rectangle(img_copy, start_point, (x, y), (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        boxes.append((start_point, end_point))
        color = get_random_color()
        colors.append(color)
        cv2.rectangle(img, start_point, end_point, color, 2)
        img_copy = img.copy()

# Create window and set callback
cv2.namedWindow("Draw Bounding Boxes")
cv2.setMouseCallback("Draw Bounding Boxes", draw_rectangle)

print("Click and drag to draw bounding boxes.")
print("Press any key when done.")

while True:
    cv2.imshow("Draw Bounding Boxes", img_copy)
    key = cv2.waitKey(1)
    if key != -1:
        break

cv2.destroyAllWindows()

cv2.imwrite("cars_bounding_boxes.jpg", img)
