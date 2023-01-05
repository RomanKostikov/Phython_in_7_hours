import os
spisok = []
#('C:\\Users\\roman\\OneDrive\\Desktop\\Для примера', ['Папка 1', 'Папка 2'], ['Файл 1.txt', 'Файл 2.txt', 'файл 3.bmp'])
for adress, dirs, files in os.walk('C:\\Users\\roman\\OneDrive\\Desktop\\Для примера'):
    for file in files:
        spisok.append(os.path.join(adress, file))         

print(spisok)
