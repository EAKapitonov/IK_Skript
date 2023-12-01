from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGBA', (3850, 2320), 'white')
imgD = ImageDraw.Draw(img)

"""Делаем ось Х"""
for i in range(300, 3750):
    for x in range(2095, 2100):
        imgD.point((i, x), fill=(0, 0, 0))

for i in range(800, 3750, 500):
    for x in range(2100, 2125):
        for z in range(5):
            imgD.point((i-z, x), fill=(0, 0, 0))

for i in range(400, 3750, 100):
    for x in range(2100, 2110):
        for z in range(5):
            imgD.point((i-z, x), fill=(0, 0, 0))

font = ImageFont.truetype("arial.ttf", 95)
for a in range(500, 3150, 500):
    word = str(4000-a)
    imgD.text((a+200, 2130), word, font=font,  fill=(0, 0, 0))


text = 'Wavenumber, cm -\u00B9'
imgD.text((1550, 2210), text, font=font,  fill=(0, 0, 0))

text = 'Transmittance, %'
imgD.text((600, 510), text, font=font,  fill=(0, 0, 0))


"""Делаем ось У"""
for i in range(100, 2100):
    for x in range(300, 305):
        imgD.point((x, i), fill=(0, 0, 0))

for i in range(300, 2100, 200):
    for x in range(275, 300):
        for z in range(5):
            imgD.point((x, i-z), fill=(0, 0, 0))

for i in range(200, 2100, 100):
    for x in range(290, 300):
        for z in range(5):
            imgD.point((x, i-z), fill=(0, 0, 0))

b = 90
for a in range(300, 2100, 200):
    word = str(b)
    imgD.text((150, a-40), word, font=font,  fill=(0, 0, 0))
    b = b - 10

text = f"%"
imgD.text((140, 100), text, font=font,  fill=(0, 0, 0))

img.save('.\picture\poloska.png')
img.show()
