from PIL import Image, ImageDraw, ImageFont
import random
import string
import os

# Function to generate random captcha text
def generate_random_text(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Function to find the next available filename
def get_next_captcha_filename():
    num = 1
    while os.path.exists(f"captcha{num}.png"):
        num += 1
    return f"captcha{num}.png"

# Function to create a captcha image
def generate_captcha_image(text):
    width, height = 250, 100
    image = Image.new('RGB', (width, height), color=(255, 255, 255))  # White background
    draw = ImageDraw.Draw(image)

    # Load font (Arial or default)
    try:
        font = ImageFont.truetype('arial.ttf', 50)
    except IOError:
        font = ImageFont.load_default()

    # Add random background symbols
    bg_symbols = "@#&*%?"
    for _ in range(15):
        char = random.choice(bg_symbols)
        x, y = random.randint(0, width), random.randint(0, height)
        color = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
        draw.text((x, y), char, font=font, fill=color)

    # Add random colored lines
    for _ in range(5):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        width_line = random.randint(1, 3)
        draw.line((x1, y1, x2, y2), fill=color, width=width_line)

    # Add random noise (dots)
    for _ in range(200):
        x, y = random.randint(0, width), random.randint(0, height)
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        draw.point((x, y), fill=color)

    # Determine total text width
    text_width = sum(font.getbbox(char)[2] for char in text) + (len(text) - 1) * 5  # Sum of letter widths + spacing
    x_offset = (width - text_width) // 2  # Center horizontally

    # Place text with tilt and offset
    for char in text:
        angle = random.randint(-15, 15)  # Slight tilt
        y_offset = random.randint(-5, 5)  # Slight vertical shift

        # Draw tilted character
        char_image = Image.new("RGBA", (50, 70), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_image)
        char_draw.text((5, 5), char, font=font, fill=(0, 0, 0))

        # Rotate character and paste onto main image
        rotated_char = char_image.rotate(angle, expand=True)
        text_y = (height - rotated_char.height) // 2 + y_offset  # Center vertically
        image.paste(rotated_char, (x_offset, text_y), rotated_char)

        x_offset += font.getbbox(char)[2] + 5  # Move to next character with spacing

    return image

# Generate random captcha text
captcha_text = generate_random_text()

# Create captcha image
captcha_image = generate_captcha_image(captcha_text)

# Get filename for new captcha
filename = get_next_captcha_filename()

# Save image with a new filename
captcha_image.save(filename)

# Show captcha
captcha_image.show()

# Print captcha text and filename
print(f"Saved as: {filename}")
print(f"Captcha text: {captcha_text}")
