from PIL import Image, ImageDraw, ImageFont
import random
import string
import os


def generate_random_text(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def get_next_captcha_filename():
    num = 1
    while os.path.exists(f"captcha{num}.png"):
        num += 1
    return f"captcha{num}.png"


def generate_captcha_image(text):
    width, height = 250, 100
    image = Image.new('RGB', (width, height), color=(255, 255, 255)) 
    draw = ImageDraw.Draw(image)

   
    try:
        font = ImageFont.truetype('arial.ttf', 50)
    except IOError:
        font = ImageFont.load_default()

   
    bg_symbols = "@#&*%?"
    for _ in range(15):
        char = random.choice(bg_symbols)
        x, y = random.randint(0, width), random.randint(0, height)
        color = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
        draw.text((x, y), char, font=font, fill=color)

    
    for _ in range(5):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        width_line = random.randint(1, 3)
        draw.line((x1, y1, x2, y2), fill=color, width=width_line)

    for _ in range(200):
        x, y = random.randint(0, width), random.randint(0, height)
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        draw.point((x, y), fill=color)

   
    text_width = sum(font.getbbox(char)[2] for char in text) + (len(text) - 1) * 5  
    x_offset = (width - text_width) // 2  

 
    for char in text:
        angle = random.randint(-15, 15)  
        y_offset = random.randint(-5, 5)  

       
        char_image = Image.new("RGBA", (50, 70), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_image)
        char_draw.text((5, 5), char, font=font, fill=(0, 0, 0))

        
        rotated_char = char_image.rotate(angle, expand=True)
        text_y = (height - rotated_char.height) // 2 + y_offset  
        image.paste(rotated_char, (x_offset, text_y), rotated_char)

        x_offset += font.getbbox(char)[2] + 5  

    return image


captcha_text = generate_random_text()


captcha_image = generate_captcha_image(captcha_text)


filename = get_next_captcha_filename()


captcha_image.save(filename)


captcha_image.show()


print(f"Saved as: {filename}")
print(f"Captcha text: {captcha_text}")
