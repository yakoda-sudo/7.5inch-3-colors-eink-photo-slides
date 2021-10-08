##
##display for 7.5 inch R/B/W 3 color eink to display better quality, need to use my script to convert picture to 3 colors 800x480
##
##
from PIL import Image
from PIL import ImageDraw
import time
import os
import random
from waveshare_epd import epd7in5b_V2
import numpy

EPD_WIDTH = 800
EPD_HEIGHT = 480

#def choose_random_loading_image(path):
#    images=os.listdir(path)
#    loading_image=random.randint(0,len(images)-1)
#   return path+images[loading_image]
# define the picture directory
picdir = '/home/pi/your_directory/bmp/'

def main():
    epd = epd7in5b_V2.EPD()
    epd.init()
#    imageB1 = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)    # 1: clear the frame
#    ImageDraw.Draw(imageB)
#    imageR1 = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
#    ImageDraw.Draw(imageR)
#    localimg = choose_random_loading_image('bmp/')
#  imageB will be save for black image imagR for red image
    localimg = random.choice(os.listdir('bmp/'))
    imageB1 = Image.open(picdir+localimg).convert('RGB')
    imageR1 = Image.open(picdir+localimg).convert('RGB')
    pixelB = imageB1.load()
    pixelR = imageR1.load()
    for i in range(imageB1.size[0]):
        for j in range(imageB1.size[1]):
            if pixelB[i, j] != (0, 0, 0):
                imageB1.putpixel((i, j), (255, 255, 255))
            else:
                pass
    for m in range(imageR1.size[0]):
        for n in range(imageR1.size[1]):
            if pixelR[m, n] != (255, 0, 0):
                imageR1.putpixel((m, n), (255, 255, 255))
            if pixelR[m, n] == (255, 0, 0):
                imageR1.putpixel((m, n), (0, 0, 0))
            else:
                pass
#    h, w = image.size
#    if h < w:
#        image = image.rotate(270, expand=True)
#    else:
#        pass
#    resized_img = image.resize((EPD_WIDTH, EPD_HEIGHT))
    imageB1 = imageB1.convert('1')
    imageR1 = imageR1.convert('1')
#    imageB1.show()
#    imageR1.show()
    epd.display(epd.getbuffer(imageB1), epd.getbuffer(imageR1))
#    time.sleep(3600)  # change the image every hour
    exit()
    main()


if __name__ == '__main__':
    main()
