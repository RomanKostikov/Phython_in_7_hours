x = ''

while len(x) < 5:
    y = input('Ввод данных: ')
    if y == 'o':
        continue

    x += y

else:
    print(x)
