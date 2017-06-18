#!/usr/bin/env python

from PIL import Image
import os
import sys

asciicode = " -.-,-:-;-i-r-s-X-A-2-5-3-h-M-H-G-S-#-9-B-&-@".split("-")
for arg in sys.argv:
    if arg != 'asciified.py':
        img = Image.open('/home/hermes/oxo-jpeg-png-toascii/img/'+arg).convert('LA')
        arg = arg.split('.')
        img = img.resize((32, 32))
        argument = ("{0}".format("grey")+arg[0])
        img.save('/home/hermes/oxo-jpeg-png-toascii/greys/'+argument+".png")
        img = Image.open('/home/hermes/oxo-jpeg-png-toascii/greys/grey{0}.png'.format(arg[0]))
        #finalimg = Image.new("LA", (32, 32))
        #grey = img.crop((0, 0, 128, 128))
        grey = img.load()
        print grey[0,0]
        # Create the final file to be made
        finalascii = open('/home/hermes/oxo-jpeg-png-toascii/avis/{0}.txt'.format(arg[0]), 'w+')

        for row in range(32):
            for column in range(32):
                rowcol = grey[row, column]
                asciinum = rowcol[0]/24

                finalascii.write(asciicode[asciinum])
            finalascii.write("\n")
        finalascii.close()
