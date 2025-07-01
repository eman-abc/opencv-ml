import cv2
import numpy as np

# angle, adjusted scale
images_info = [
    ('street.jpg', 45, 0.7),
    ('cars.jpg', 90, 1.0),
    ('kitten.jpg', 135, 0.6)
]

for filename, angle, scale in images_info:
    img = cv2.imread(filename)
    if img is None:
        print(f"Error loading {filename}")
        continue

    h, w = img.shape[:2]
    center = (w // 2, h // 2)

    # rot. matrix with manual scale
    M = cv2.getRotationMatrix2D(center, angle, scale)

    # geometry.. size of new window else image is cropped even w a manual adj of scale
    radians = np.deg2rad(angle)
    cos = np.abs(np.cos(radians)) * scale
    sin = np.abs(np.sin(radians)) * scale
    new_w = int(h * sin + w * cos)
    new_h = int(h * cos + w * sin)

    # adjust rotation matrix to shift image to center of new canvas
    M[0, 2] += (new_w / 2) - center[0] #x translation
    M[1, 2] += (new_h / 2) - center[1] #y translation

    rotated = cv2.warpAffine(img, M, (new_w, new_h))

    # display in resizable window
    window_name = f"{filename} - Rotated {angle}°"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
