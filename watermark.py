from PIL import Image, ImageFont, ImageDraw
import os


def watermark(watermark, image, file):
    # Defines the desired size
    size_50 = ((i.size[0]/2), (i.size[1]/2))
    # splits file name from file extension
    fn, fext = os.path.splitext(f)
    # Resized images to 50% width and height
    # Defines location of watermark
    size_50_wm = ((wm.size[0]/1.3), (wm.size[1]/1.3))
    wm.thumbnail(size_50_wm)
    isize = i.size
    wmsize = wm.size
    posX = 25
    posY = isize[1] - wmsize[1] - posX
    imark = i.paste(wm, (posX,posY), wm)
    # Saves the resized image
    i.save('./output/{}{}'.format(fn,fext))

wm = '' 
while wm == '' or  'png' not in wm:
    wm = Image.open(input('\nWhat is the file name of your watermark? \nEnsure that you type the ENTIRE file name with extension (eg:filename.png) \n\nEnter Filename: '))

# Iterates through all files in the input directory
for f in os.listdir('./input/'):
# Iterates through only JPEG files
    if f.endswith('.jpg'):
        i = Image.open('./input/' + f)
        watermark(wm,i,f)



