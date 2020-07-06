from PIL import Image, ImageOps, ImageDraw
import os

def crop(name):
    SPEAKER_FOLDER = os.getcwd() + "/SPEAKERS/" 

    size = (206, 206)
    mask = Image.new('L', (200,200), 0)

    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + size, fill=255)

    print("Rendering",name)
    # Mast the profile picture to the cirlce
    im = Image.open(SPEAKER_FOLDER+name)
    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)

    return (output,mask)