from PIL import Image, ImageDraw, ImageFont


image_paths = ['street.jpg', 'cars.jpg', 'kitten.jpg', 'circuit.jpg']


for image_path in image_paths:
    img = Image.open(image_path)
    print(f"Image '{image_path}' loaded with dimensions: {img.width}x{img.height}")

    # stretch image
    width, height = img.size
    stretched_width = int(width * 1.5)
    stretched_height = int(height * 0.7)

    stretched_img = img.resize((stretched_width, stretched_height))

    draw = ImageDraw.Draw(stretched_img)
    # custom font cz default too small
    font = ImageFont.truetype("arial.ttf", size=50)

    draw.line((0, 0, stretched_width - 1, stretched_height - 1), fill=(255, 0, 0), width=4)
    draw.ellipse((stretched_width // 4, stretched_height // 4, stretched_width * 3 // 4, stretched_height * 3 // 4), outline=(0, 0, 0), width=6)

# place text
    text = "Sundas Eman"
    text_position = (int(stretched_width * 0.07), int(stretched_height * 0.7))
    draw.text(text_position, text, fill=(0, 165, 255), font=font)   

# rotate the image
    stretched_img = stretched_img.rotate(45, expand=True)
    stretched_img.show(title=f"Modified {image_path}")
    stretched_img.save(f"stretched_{image_path}")