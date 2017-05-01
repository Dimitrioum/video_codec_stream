# -*- coding: utf-8 -*-
from PIL import Image

# определение констант
_LUMA_WIDTH = 128  # ширина блока яркости
_LUMA_HEIGHT = 96  # высота блока яркости
_CHROMA_WIDTH = _LUMA_WIDTH / 2  # ширина блока цвета
_CHROMA_HEIGHT = _LUMA_HEIGHT / 2  # высота блока цвета

image = Image.open('nature.jpg')  # Открываем изображение.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.

# считывание компонент R G B в кадре
R = [[pix[i, j][0] for j in range(height)] for i in range(width)]
G = [[pix[i, j][1] for j in range(height)] for i in range(width)]
B = [[pix[i, j][2] for j in range(height)] for i in range(width)]

# RGB to YUV
Y = [[(pix[i, j][0] * 0, 299 + pix[i, j][1] * 0, 587 + pix[i, j][2] * 0, 114) for j in range(height)] for i in
     range(width)]
U = [[(-pix[i, j][0] * 0, 14713 - pix[i, j][1] * 0, 28886 + pix[i, j][2] * 0, 436 + 128) for j in range(height)] for i
     in range(width)]
V = [[(pix[i, j][0] * 0, 615 - pix[i, j][1] * 0, 51499 - pix[i, j][2] * 0, 10001 + 128) for j in range(height)] for i in
     range(width)]

# NAL юниты
sps = [0x00, 0x00, 0x00, 0x01, 0x67, 0x42, 0x00, 0x0a, 0xf8, 0x41,
       0xa2]  # 1 / stream - адресует последовательность кодированных кадров
pps = [0x00, 0x00, 0x00, 0x01, 0x68, 0xce, 0x38,
       0x80]  # 1 / stream - адресует расшифровку одного или несколько кадров в полученной последовательности
slice_header = [0x00, 0x00, 0x00, 0x01, 0x05, 0x88, 0x84, 0x21, 0xa0]  # 1 / video frame
macroblock_header = [0x0d, 0x00]  # 1 / macroblock

f = open('macroblock_data.csv', 'w')


# macroblock data
def macroblock(i, j):
    if not ((i == 0) & (j == 0)): f.write(str(macroblock_header))  # спецификация h.264 ЗАЧЕМ ??
    # macroblock_header получают все макроблоки, кроме i = 0, j = 0.

    for x in range(width):
        for y in range(height):
            f.write(str(R[x][y]))  # либо Y[x][y]

    for x in range(width):
        for y in range(height):
            f.write(str(G[x][y]))  # либо U[x][y]

    for x in range(width):
        for y in range(height):
            f.write(str(B[x][y]))  # либо V[x][y]


if __name__ == '__main__':

    f.write(str(sps))
    f.write(str(pps))
    while not f.closed:

        f.write(str(slice_header))
        for i in range(width):
            for j in range(height):
                macroblock(i, j)
        f.write('0x80')
        f.close()
