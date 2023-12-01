import csv
from PIL import Image, ImageDraw, ImageFont

lang = int(input("1-RUS, 2-ENG  "))
if lang == 1:
    img = Image.open('.\picture\RUS.png')
elif lang == 2:
    img = Image.open('.\picture\ENG.png')
else:
    exit()

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
e = 1
font = ImageFont.truetype("arial.ttf", 50)
while e == 1:
    m = input('Если хотите добавить метку напишите волновое число'
              'Если Нет то введите "n"  ')
    if m == 'n':
        e = 0
    else:
        m = int(m)
        count = 0
        with open('sample.csv', 'r', encoding='utf-8') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                count = count + 1
                if count < 6:
                    continue
                else:
                    x = float(row[0])
                    x = int(x)
                    if x == m:
                        h = float(row[1]) * 20
                        h = int(h)
                        imgD.line((4305 - x, 2100 - h, 4305 - x, 2200 - h), fill=(0, 0, 0), width=3)
                        word = str(x)
                        imgD.text((4240 - x, 2200 - h), word, font=font, fill=(0, 0, 0))

img.save('point.png')
img.show()
