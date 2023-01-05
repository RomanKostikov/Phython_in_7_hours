##import os
##
##list_paths = []
##
##for adress, papka, file in os.walk('C:\\'):
##    for i in file:
##        full_path = os.path.join(adress, i)
##        list_paths.append(full_path)

##'r' открыть для чтения (по умолчанию)
##'t' открыть в текстововм режиме (по умолчанию)
##'w' открыть для записи, содержимое файлов удаляется, если файла нет, создается новый
##'a' открыть для дозаписи в конец файла, если файла нет, созается новый
##'b' открыть в бинарном режиме
##'+' открыть для чтения и записи 'r+', 'w+', 'a+'

##r = open('text.txt', 'w')
##r.write('Строка текста')
##r.close()

##r = open('text.txt')
##u = r.read()
##print(u)
##r.close()

##r = open('text.txt', 'w')
##for x in list_paths:
##    r.write(x + '\n')
##    
##r.close()

##r = open('text.txt')
##for i in r:
##    if 'PRO100 DEMO' in i:
##        print(i)
##    
##r.close()

r = open('КОМПАС-3D LT V9.exe', 'rb')
y = open('Копия КОМПАС-3D LT V9. exe', 'wb')

while True:
    var = r.read(1048576)
    print(var.__sizeof__())
    if var.__sizeof__() == 33:
        break
    
    y.write(var)
    

print('Контрол')
r.close()
y.close()
