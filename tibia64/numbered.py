import os, shutil

import PIL
from PIL import Image

im = Image.new('RGB', (32, 32), (255, 0, 255))
im.save('sprites/png/numbered/0001.png')
im.save('sprites/png/numbered/1087.png')

for f in os.listdir('sprites/png'):
    if '.png' in f:
        newf = f
        while len(newf) < 8:
            newf = '0' + newf
        shutil.copy2('sprites/png/' + f, 'sprites/png/numbered/' + newf)
        print(newf)
