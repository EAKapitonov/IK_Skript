from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGBA', (3800, 2300), 'white')
imgD = ImageDraw.Draw(img)

"""Делаем ось Х"""
for i in range(250, 3700):
    for x in range(2095, 2100):
        imgD.point((i, x), fill=(0, 0, 0))

for i in range(750, 3700, 500):
    for x in range(2100, 2125):
        for z in range(5):
            imgD.point((i-z, x), fill=(0, 0, 0))

for i in range(350, 3700, 100):
    for x in range(2100, 2110):
        for z in range(5):
            imgD.point((i-z, x), fill=(0, 0, 0))

font = ImageFont.truetype("arial.ttf", 95)
for a in range(500, 3150, 500):
    word = str(4000-a)
    imgD.text((a+150, 2130), word, font=font,  fill=(0, 0, 0))

text = 'Волновое число, cm -\u00B9'
imgD.text((1550, 2200), text, font=font,  fill=(0, 0, 0))

text = 'Отн. единиц'
imgD.text((100, 2200), text, font=font,  fill=(0, 0, 0))


"""Делаем ось У"""
for i in range(100, 2100):
    for x in range(250, 255):
        imgD.point((x, i), fill=(0, 0, 0))

for i in range(300, 2100, 200):
    for x in range(225, 250):
        for z in range(5):
            imgD.point((x, i-z), fill=(0, 0, 0))

for i in range(200, 2100, 100):
    for x in range(240, 250):
        for z in range(5):
            imgD.point((x, i-z), fill=(0, 0, 0))

"""
b = 90
for a in range(300, 2100, 200):
    word = str(b)
    imgD.text((150, a-40), word, font=font,  fill=(0, 0, 0))
    b = b - 10
"""

img.save('poloska.png')
img.show()
