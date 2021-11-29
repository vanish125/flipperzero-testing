#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

import sys

from PIL import Image
from PIL import ImageChops

image_path = "out"

name1 = sys.argv[1]
name1 = sys.argv[2]



image_one = Image.open(f'{image_path}/{name1}').convert('RGB')
image_two = Image.open(f'{image_path}/{name2}').convert('RGB')

diff = ImageChops.difference(image_one, image_two)

if diff.getbbox():
    print("Ok")
else:
    print("Error")
