import os

import PIL
from PIL import Image

sprite_size = 32

width  = 2048
height = 2048

spritesheet = Image.new('RGBA', (width, height), (0, 0, 0, 0))

x = 0
y = 0

for f in os.listdir('sprites/png/numbered/'):

    if '.png' in f:

        sprite = Image.open('sprites/png/numbered/' + f)

        spritesheet.paste(sprite, (x, y))

        x += sprite_size

        if x == width:
            x = 0
            y += sprite_size
 
spritesheet.save('tiles.png')
