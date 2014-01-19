import sys, os, struct

import PIL
from PIL import Image

palette_r = []
palette_g = []
palette_b = []

try:

    with open('tibia.pal', 'rb') as f:

        for i in range(0, 256):

            bytes = f.read(1)
            r = struct.unpack('b', bytes)[0]

            palette_r.append(r)

            bytes = f.read(1)
            g = struct.unpack('b', bytes)[0]

            palette_g.append(g)

            bytes = f.read(1)
            b = struct.unpack('b', bytes)[0]

            palette_b.append(b)

    f.close()

except IOError:

    print 'Error: tibia.pal file not found!'
    print 'Using hard-coded palette...'

    palette_r = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-103,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-52,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    palette_g = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,51,51,51,51,51,51,102,102,102,102,102,102,-103,-103,-103,-103,-103,-103,-52,-52,-52,-52,-52,-52,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,51,51,51,51,51,51,102,102,102,102,102,102,-103,-103,-103,-103,-103,-103,-52,-52,-52,-52,-52,-52,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,51,51,51,51,51,51,102,102,102,102,102,102,-103,-103,-103,-103,-103,-103,-52,-52,-52,-52,-52,-52,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,51,51,51,51,51,51,102,102,102,102,102,102,-103,-103,-103,-103,-103,-103,-52,-52,-52,-52,-52,-52,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,51,51,51,51,51,51,102,102,102,102,102,102,-103,-103,-103,-103,-103,-103,-52,-52,-52,-52,-52,-52,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,51,51,51,51,51,51,102,102,102,102,102,102,-103,-103,-103,-103,-103,-103,-52,-52,-52,-52,-52,-52,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    palette_b = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,0,51,102,-103,-52,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


'''
with open('tibia.pal.txt', 'w') as f:

    for i in range(0, 256):

        f.write(str(palette_r[i]))
        f.write('\n')

        f.write(str(palette_g[i]))
        f.write('\n')

        f.write(str(palette_b[i]))
        f.write('\n')

f.close()

with open('tibia.pal.r.txt', 'w') as f:

    f.write('a = ')
    f.write('[')

    for i in range(0, 256):

        f.write(str(palette_r[i]))
        f.write(',')

    f.write(']')

f.close()

with open('tibia.pal.g.txt', 'w') as f:

    f.write('a = ')
    f.write('[')

    for i in range(0, 256):

        f.write(str(palette_g[i]))
        f.write(',')

    f.write(']')

f.close()

with open('tibia.pal.b.txt', 'w') as f:

    f.write('a = ')
    f.write('[')

    for i in range(0, 256):

        f.write(str(palette_b[i]))
        f.write(',')

    f.write(']')

f.close()
'''

print('Old Tibia Sprite Extractor')

try:

    with open('TIBIA.SPR', 'rb') as f:

        if not os.path.exists('sprites'):

            print('Creating sprites folder...')

            os.makedirs('sprites')

        print('Extracting TIBIA.SPR...')

        bytes = f.read(2)
        num_sprites = struct.unpack('h', bytes)[0]

        num_sprites -= 1

        print('Number of sprites: ' + str(num_sprites))

        f.seek(4, 1)

        for i in range(0, num_sprites):

            bytes = f.read(2)
            sprite_id = struct.unpack('h', bytes)[0]

            #print('Sprite ID: ' + str(sprite_id))

            im = Image.new('RGB', (32, 32), (255, 0, 255))

            pixels = im.load()

            bytes = f.read(2)
            num_bytes_for_sprite = struct.unpack('h', bytes)[0]

            #print('Number of bytes for sprite: ' + str(num_bytes_for_sprite))

            num_bytes_for_sprite -= 2

            bytes_left = num_bytes_for_sprite

            position_in_data = 0

            while bytes_left > 0:

                bytes = f.read(2)

                num_transparent_pixels = struct.unpack('h', bytes)[0]

                #print('Number of transparent pixels: ' + str(num_transparent_pixels))

                position_in_data += num_transparent_pixels
     
                bytes = f.read(1)
                num_rgb_pixels = struct.unpack('b', bytes)[0]

                #print('Number of RGB pixels: ' + str(num_rgb_pixels))

                bytes_left -= 3

                for j in range(0, num_rgb_pixels):

                    bytes = f.read(1)
                    color = struct.unpack('b', bytes)[0]

                    #print(color)

                    r = palette_r[color] & 0xFF
                    g = palette_g[color] & 0xFF
                    b = palette_b[color] & 0xFF

                    pixels[position_in_data % 32, (31 - ((position_in_data - position_in_data % 32) / 32))] = (r, g, b) #color

                    position_in_data += 1

                    bytes_left -= 1

            im.save('sprites/' + str(sprite_id) + '.bmp')

            del im

            sys.stdout.write('.')

    print('')
    print('Done!')

    f.close()

except IOError:

   print 'Error: TIBIA.SPR file not found!'
