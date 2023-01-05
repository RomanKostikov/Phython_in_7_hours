import os
import time
spisok = []
#('C:\\Users\\roman\\OneDrive\\Desktop\\Для примера', ['Папка 1', 'Папка 2'], ['Файл 1.txt', 'Файл 2.txt', 'файл 3.bmp'])
for adress, dirs, files in os.walk('C:\\Users\\roman\\OneDrive\\Desktop\\Для примера'):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400 and '.txt' in full:
            spisok.append(full)         

print(spisok)
