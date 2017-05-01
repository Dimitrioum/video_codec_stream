# -*- coding: utf-8 -*-
import random
from PIL import Image, ImageDraw

image = Image.open('nature.jpg') #Открываем изображение.
width = image.size[0] #Определяем ширину.
height = image.size[1] #Определяем высоту.
pix = image.load() #Выгружаем значения пикселей.

# считывание компонент R G B в кадре
R = [[pix[i,j][0] for j in range(height)] for i in range(width)]
G = [[pix[i,j][1] for j in range(height)] for i in range(width)]
B = [[pix[i,j][2] for j in range(height)] for i in range(width)]



