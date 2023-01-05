h = ['https:\\www.сайт.com', 'https:\\www.какойтосайт.net',
     'https:\\www.левыйсайт.com', 'https:\\www.другойсайт.com',
     'https:\\www.сайтишка.net', 'https:\\www.сайтец.com']
import os

n = [x for x in os.walk('C:\\')] #генератор списка
print('здесь')

z = (y for y in os.walk('C:\\')) #выражение генератора
print('тут')
