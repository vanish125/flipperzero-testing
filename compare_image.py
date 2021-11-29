#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

import sys

from PIL import Image
from PIL import ImageChops

image_path = "out"
orig_path = "orig"

name = sys.argv[1]

image_one = Image.open(f'{image_path}/{name}').convert('RGB')
image_two = Image.open(f'{orig_path}/{name}').convert('RGB')

diff = ImageChops.difference(image_one, image_two).getbbox()

if diff==None:
    print("Ok")
else:
    print("Error")
