from PIL import Image, ImageDraw, ImageFont

def overlay_text_on_image(image_path, text, position, output_path, font_path="arial.ttf", font_size=30, text_color=(0, 0, 0)):
    # Load the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Add text to image
    draw.text(position, text, font=font, fill=text_color)

    # Save the image with overlay text as PNG to preserve transparency
    image.save(output_path, format="PNG")
    print(f"Image saved at {output_path}")

# Example usage
overlay_text_on_image("image.png", "Hello, World!", position=(25, 1643), output_path="output_image_with_text.png")
