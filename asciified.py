#!/usr/bin/env python

from PIL import Image
import os
# Open an arbitrary image and save it as greyscale
#TODO add an argument to be passed.
img = Image.open('kitten.jpeg').convert('LA')
img = img.resize((32, 32))
img.save('greyscale.png')


asciicode = " -.-,-:-;-i-r-s-X-A-2-5-3-h-M-H-G-S-#-9-B-&-@".split("-")

img = Image.open('greyscale.png')
finalimg = Image.new("LA", (32, 32))
#grey = img.crop((0, 0, 128, 128))
grey = img.load()
print grey[0,0]
# Create the final file to be made
finalascii = open('asciified.txt', 'w+')

for row in range(32):
    for column in range(32):
        rowcol = grey[row, column]
        asciinum = rowcol[0]/24

        finalascii.write(asciicode[asciinum])
    finalascii.write("\n")
finalascii.close()
