import csv
from PIL import Image, ImageDraw


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
            imgD.line((4305 - x, 2100 - h, 4305 - x2, 2100 - h2), fill=(0, 0, 0), width=6)
            x2 = x
            h2 = h

img.save('point.png')

