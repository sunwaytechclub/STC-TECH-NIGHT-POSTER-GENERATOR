from PIL import Image, ImageOps, ImageDraw,ImageFont
import os
import cropping
import csv

TOP_RIGHT = (288,400)
TEXT_SIZE = 18
TEMPLATE_IMG = "TNT1.png"
FONT_TTF_FILE = "Montserrat-SemiBold.otf"

    
def output_speaker(speaker):
    img = Image.open(TEMPLATE_IMG)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_TTF_FILE, TEXT_SIZE)

    positions = speaker["POSITIONS"]
    name = speaker['PROFILE PIC'].replace(".jpg",'')

    # Get the cropped image
    cropped_image,mask = cropping.crop(speaker['PROFILE PIC'])

    # Populate positions
    size = draw.multiline_textsize(positions,font=font)
    draw.multiline_text((TOP_RIGHT[0]- size[0], TOP_RIGHT[1]),positions, (255, 255, 255), font=font,align="right")

    # Populate image
    img.paste(cropped_image,(122,99),mask)

    # Populate Name
    name_top_left = (328.31,282.333)
    name_text_size = 30
    name_font = ImageFont.truetype(FONT_TTF_FILE, name_text_size)
    draw.text(name_top_left,speaker['NAME'],font=name_font)

    # Populate Topic
    topic_top_left = (328.31,350.333)
    topic_text_size = 30
    topic_font = ImageFont.truetype(FONT_TTF_FILE, topic_text_size)
    draw.text(topic_top_left,speaker['ACTIVITY'],font=topic_font)
    
    #POPULATING Why
    why_top_left = (328.31,450.333)
    why_text_size = 25
    why_font = ImageFont.truetype(FONT_TTF_FILE, why_text_size)
    draw.text(why_top_left,speaker['WHY'],font=why_font)
    
    #POPULATING What
    what_top_left = (328.31,574.333)
    what_text_size = 25
    what_font = ImageFont.truetype(FONT_TTF_FILE, what_text_size)
    draw.text(what_top_left,speaker['WHAT'],font=what_font)
    
    img.save(f'output/{name}.jpg')
    print('Generated', name)

if __name__ == "__main__":

    # Populate the placeholders
    with open('CREDENTIALS.csv') as f:
        csv_reader =csv.DictReader(f)
        #get fieldnames from DictReader object and store in list
        headers = csv_reader.fieldnames

        for line in csv_reader:
            output_speaker(line)

