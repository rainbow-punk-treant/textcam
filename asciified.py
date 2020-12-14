#!/usr/bin/env python

from PIL import Image
import os
import sys

asciicode = " -.-,-:-;-i-r-s-X-A-2-5-3-h-M-H-G-S-#-9-B-&-@".split("-")
for arg in sys.argv:
    if arg != 'asciified.py':
        img = Image.open('/home/entropy/Code/oxo-jpeg-png-toascii/img/'+arg)
        arg = arg.split('.')
        colours = []
        img = img.resize((32, 32))
        argument = ("{0}".format("grey")+arg[0])
        img.save('/home/entropy/Code/oxo-jpeg-png-toascii/greys/'+argument+".png")
        img = Image.open('/home/entropy/Code/oxo-jpeg-png-toascii/greys/grey{0}.png'.format(arg[0]))
        #finalimg = Image.new("LA", (32, 32))
        #grey = img.crop((0, 0, 128, 128))
        grey = img.load()
        # print(grey[0,0])
        # Create the final file to be made
        finalascii = open('/home/entropy/Code/oxo-jpeg-png-toascii/avis/{0}.txt'.format(arg[0]), 'w+')
        p = ""
        for y in range(32):
            for x in range(32):
                sample = (x, y)
                pixel = img.getpixel(sample)
                colours.append(pixel)
                # colours.append("BREAK")
                rowcol = grey[y, x]
                asciinum = int(rowcol[0]/24)
                p += "\033[48;2;"+str(pixel[0])+";"+str(pixel[1])+";"+str(pixel[2])+"m"+str(asciicode[asciinum])+"\033[0m"
                finalascii.write("\033[48;2;"+str(pixel[0])+";"+str(pixel[1])+";"+str(pixel[2])+"m"+str(asciicode[asciinum])+"\033[0m")
            p += "\n"
            finalascii.write("\n")
        finalascii.close()
        print(p)

