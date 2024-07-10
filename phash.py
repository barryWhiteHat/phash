from PIL import Image, ImageDraw
import sys 

import pdb 
def phash(filename):
    im = Image.open(filename)
    # resize to 64 pixles
    out = im.resize((8,8))
    # gray scale 
    out = out.convert('L')
    px = out.load()
    average = 0 

    # calculate average
    for x in range (0,8):
        for y in range(0,8):
            average += px[x,y]


    average = average / 64

    phash = "" 
    for x in range(0,8): 
        for y in range (0,8):
            if (px[x,y] > average):
                phash += "1"
            else:
                phash += "0"
    phash = int(phash,2)
    out = hex(phash)
    while len(out) < 18: 
        out += "0"

    return(out)


if __name__ == "__main__":
    pics = sys.argv[1:] 
    for pic in pics:
        out = phash(pic)
        print(out)
