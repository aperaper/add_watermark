#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Xry'

import PIL
from PIL import Image, ImageDraw, ImageFont


# 加文字水印
# ft = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
#
# imageFile = 'C:/Users/xy/Desktop/ScreenClip.png'
# im = Image.open(imageFile)
#
# draw = ImageDraw.Draw(im)
# draw.text((100, 20), 'water12', (255, 0, 0), font=ft)

class AddWaterMark(object):
    def add_mark(self, image_path, image_name, mark):
        image = image_path + image_name
        mark = Image.open(mark)
        if mark.mode != 'RGBA':
            mark = mark.convert('RGBA')
        im = Image.open(image)
        layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
        layer.paste(mark, (im.size[0] - mark.size[0], im.size[1] - mark.size[1]))
        output = Image.composite(layer, im, layer)
        output.save(image_path + 'WM-' + image_name)


ad = AddWaterMark()
ad.add_mark('C:/Users/xy/Desktop/', 'lena123321321.jpg', 'ScreenClip.jpg')
print(123)
print(456)
print(789)
print(000)
print(00000)
print(11111)
