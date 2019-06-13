#
# hexbot.py - noops challenge
#
# (c) gdifiore 2019 <difioregabe@gmail.com>
#

import requests
from PIL import Image
import numpy as np
import json

def hexbot_start():
    print("Hello! 🤖 🤖 🤖 🤖 🤖")

def hexbot_fetch():
    url = 'https://api.noopschallenge.com/hexbot?count=5'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def hexbot_create(data):
    pix = []
    for x in range (0,5):
        hex = data['colors'][x]['value']
        h = hex.lstrip('#')
        rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        pix.append(rgb)

    pixels = []
    pixels.append(pix)

    array = np.array(pixels, dtype=np.uint8)

    new_image = Image.fromarray(array)
    new_image.save('nopbot.png')

    print("image created!")

hexbot_start()
data = hexbot_fetch()
hexbot_create(data)