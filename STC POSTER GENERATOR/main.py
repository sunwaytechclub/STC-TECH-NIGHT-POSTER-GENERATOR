from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
import os

TEXT_Y_PIXEL = 680
TEXT_SIZE = 36
TEMPLATE_IMG = "poster.png"
FONT_TTF_FILE = "Montserrat-medium.otf"

def output_poster(name):
    img = Image.open(TEMPLATE_IMG)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype(FONT_TTF_FILE, TEXT_SIZE)
    # draw.text((x, y),"Sample Text",(r,g,b))
    img_width,_  = img.size
    text_width,_ = font.getsize(name.upper())

    draw.text((img_width/2 - text_width/2, TEXT_Y_PIXEL),
              name.upper(), (255, 255, 255), font=font)
    now = datetime.now()
    img.save(f'output/{datetime.timestamp(now)}.jpg')
    print('Generated')


if __name__ == "__main__":
    os.makedirs('output', exist_ok=True)
    print("The event detail will be rendered in the format:\n\t EPISODE {number} {date} {time}")
    number = input("Episode Number (e.g. 1):")
    date = input("Date (e.g. 13.01.2020):")
    time = input("Time (e.g. 8.00PM):")
    name = "EPISODE "+number +"   "+date+"  "+time
    output_poster(name)   