import csv
from PIL import Image, ImageDraw

#img = Image.new('RGBA', (3750, 2300), 'white')
img = Image.open('poloska.png')
imgD = ImageDraw.Draw(img)
count = 0
x2 = 0
h2 = 0
with open('sample.csv', 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        count = count + 1
        if count < 6:
            continue
        else:
            x = float(row[0])
            x = int(x)
            h = float(row[1]) * 20
            h = int(h)
            if x2 == 0:
                x2 = x
                h2 = h
            #imgD.point((4200 - x, 2100 - h), fill=(0, 0, 0))
            #imgD.point((4200 - x, 2099 - h), fill=(0, 0, 0))
            #imgD.point((4200 - x, 2101 - h), fill=(0, 0, 0))
            #imgD.point((4200 - x, 2098 - h), fill=(0, 0, 0))
            #imgD.point((4200 - x, 2102 - h), fill=(0, 0, 0))
            imgD.line((4205 - x, 2100 - h, 4205 - x2, 2100 - h2), fill=(0, 0, 0), width=6)
            x2 = x
            h2 = h

img.save('point.png')
img.show()

