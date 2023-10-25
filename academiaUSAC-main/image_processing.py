from PIL import Image, ImageDraw

def process_image(file_path):
    image = Image.open(file_path)

    # Get the dimensions of the original image
    width, height = image.size

    # Determine new dimensions that fit within 200x200 while maintaining aspect ratio
    if width > height:
        new_width = 200
        new_height = int((height / width) * 200)
    else:
        new_height = 200
        new_width = int((width / height) * 200)

    # Resize the image
    image_resized = image.resize((new_width, new_height))

    # Create a new blank RGBA image with 200x200 dimensions
    final_image = Image.new('RGBA', (200, 200))

    # Calculate position to paste the resized image onto the final image
    paste_x = (200 - new_width) // 2
    paste_y = (200 - new_height) // 2

    # Paste the resized image onto the final image
    final_image.paste(image_resized, (paste_x, paste_y))

    # Create mask
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=255)

    # Apply mask
    result = Image.new('RGBA', (200, 200))
    result.paste(final_image, mask=mask)

    return result
