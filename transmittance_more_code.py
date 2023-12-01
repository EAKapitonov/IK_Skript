import csv
from PIL import Image, ImageDraw, ImageFont

lang = int(input("1-RUS, 2-ENG  "))
if lang == 1:
    img = Image.open('.\picture\RUS_MORE.png')
elif lang == 2:
    img = Image.open('.\picture\ENG_MORE.png')
else:
    exit()
imgD = ImageDraw.Draw(img)
color = {1: 'black', 2: 'red', 3: 'green', 4: 'yellow', 5: 'grey', 6: 'blue'}
count_graff = input("Введите количество графиков")
k2 = float(input("Введите во сколько раз сжать график. Знак дроби точка "))
k = float(input("Введите коэффициент расстояния между графиками от 1 и выше. Знак дроби точка "))
for c in range(1, 1+int(count_graff)):
    count = 0
    x2 = 0
    h2 = 0
    print("1-black "
          "2-red "
          "3-green "
          "4-yellow "
          "5-grey "
          "6-blue")
    color_graff = int(input(f"Выберите цвет графика{c}"))
    with open(f'sample{c}.csv', 'r', encoding='utf-8') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            count = count + 1
            if count < 6:
                continue
            else:
                x = float(row[0])
                x = int(x)
                h = float(row[1]) * 20 / k2
                h = int(h)
                if x2 == 0:
                    x2 = x
                    h2 = h
                imgD.line((4255 - x, 100 + 2000/k2 - h + (c-1)*100*k, 4255 - x2, 100 + 2000/k2 - h2 + (c-1)*100*k), fill=(color[color_graff]), width=6)
                x2 = x
                h2 = h
    e = 1
    font = ImageFont.truetype("arial.ttf", 50)
    while e == 1:
        m = input(f'Если хотите добавить метку для {c} графика напишите волновое число'
                  'Если Нет то введите "n"  ')
        if m == 'n':
            e = 0
        else:
            m = int(m)
            count = 0
            with open(f'sample{c}.csv', 'r', encoding='utf-8') as f:
                csvreader = csv.reader(f)
                for row in csvreader:
                    count = count + 1
                    if count < 6:
                        continue
                    else:
                        x = float(row[0])
                        x = int(x)
                        if x == m:
                            h = float(row[1]) * 20 / k2
                            h = int(h)
                            imgD.line((4255 - x, 100 + 2000/k2 - h + (c-1)*100*k, 4255 - x, 200 + 2000/k2 - h + (c-1)*100*k), fill=(color[color_graff]), width=3)
                            word = str(x)
                            imgD.text((4215 - x, 200 + 2000/k2 - h + (c-1)*100*k), word, font=font, fill=(0, 0, 0))

img.save('point.png')
img.show()
