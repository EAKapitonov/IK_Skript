from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGBA', (3750, 2300), 'white')
imgD = ImageDraw.Draw(img)

"""Делаем ось Х"""
for i in range(200, 3650):
    for x in range(2095, 2100):
        imgD.point((i, x), fill=(0, 0, 0))

for i in range(700, 3650, 500):
    for x in range(2100, 2125):
        for z in range(5):
            imgD.point((i-z, x), fill=(0, 0, 0))

for i in range(300, 3650, 100):
    for x in range(2100, 2110):
        for z in range(5):
            imgD.point((i-z, x), fill=(0, 0, 0))

font = ImageFont.truetype("arial.ttf", 100)
for a in range(500, 3150, 500):
    word = str(4000-a)
    imgD.text((a+120, 2130), word, font=font,  fill=(0, 0, 0))


text = u'Wavenumber, cm\u207B\u00B9'
imgD.text((1700, 2205), text, font=font,  fill=(0, 0, 0))


"""Делаем ось У"""
for i in range(100, 2100):
    for x in range(200, 205):
        imgD.point((x, i), fill=(0, 0, 0))

for i in range(300, 2100, 200):
    for x in range(175, 200):
        for z in range(5):
            imgD.point((x, i-z), fill=(0, 0, 0))

for i in range(200, 2100, 100):
    for x in range(190, 200):
        for z in range(5):
            imgD.point((x, i-z), fill=(0, 0, 0))

b = 90
for a in range(300, 2100, 200):
    word = str(b)
    imgD.text((50, a-40), word, font=font,  fill=(0, 0, 0))
    b = b - 10

text = f"%"
imgD.text((40, 100), text, font=font,  fill=(0, 0, 0))

img.save('poloska.png')
img.show()
