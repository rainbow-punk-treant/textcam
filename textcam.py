#!/usr/bin/env python

from PIL import Image
import os
import sys

asciicode = " -.-,-:-;-i-r-s-X-A-2-5-3-h-M-H-G-S-#-9-B-&-@".split("-")
if len(sys.argv) > 1:
    img = Image.open(sys.argv[1])

    colours = []
    img = img.resize((32, 32))
    grey = img.load()
    finalascii = open('/home/entropy/Code/textcam/avis/temp_photo.txt', 'w+')
    p = ""
    for y in range(32):
        for x in range(32):
            sample = (x, y)
            pixel = img.getpixel(sample)
            colours.append(pixel)
            rowcol = grey[y, x]
            asciinum = int(rowcol[0]/24)
            p += "\033[48;2;"+str(pixel[0])+";"+str(pixel[1])+";"+str(pixel[2])+"m"+str(asciicode[asciinum])+"\033[0m"
            finalascii.write("\033[48;2;"+str(pixel[0])+";"+str(pixel[1])+";"+str(pixel[2])+"m"+str(asciicode[asciinum])+"\033[0m")
        p += "\n"
        finalascii.write("\n")
    finalascii.close()
    # print(p)

