m = 'stroka text'
count = 0

for i in m:
    if i == 't' :
        print('В строке есть буква t')
        count += 1
    if i == 'a':
        break
else:
    print('Цикл завершен, букв t', count)

print('Программа работает дальше')
