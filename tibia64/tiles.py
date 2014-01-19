import os

import PIL
from PIL import Image

sprite_size = 32

num_sprites = 3316 + 2

num_pixels_y = num_sprites * sprite_size

width  = 2048
height = 2048 #((num_pixels_y / width) * sprite_size) + sprite_size

spritesheet = Image.new('RGBA', (width, height), (0, 0, 0, 0))

index = 0

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

        index = index + 1
 
spritesheet.save('tiles.png')
