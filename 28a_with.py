##r = open('file.txt', 'a')
##r.write('something' + '\n')
##10/0
##r.write('что-то')
##r.close()
##
##print('Все норм')

##Используем контексный менеджер
##with open('file.txt', 'a') as r:
##    r.write('something' + '\n')
##    10/0
##    r.write('что-то')
##   
##print('Все норм')

##обработка ошибки
r = open('file.txt', 'a')
try:
    r.write('something' + '\n')
    10/0
    r.write('что-то')
finally:
    r.close()

print('Все норм')
