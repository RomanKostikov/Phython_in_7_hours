s = 'sTroka texta'

##print(s[0:5]) #вывели срез
##print(s[5])#вывели отдельный симвл
##print('str' in s) #проверили подстроку в строке

s1 = s.upper() #все в верхний регистр
print(s1)
s2 = s.lower() #все в нижний регистр
print(s2)
s3 = s.capitalize() #первая в верхний регистр
print(s3)
#print(s)

path = 'C:/Users/roman/OneDrive/Desktop/Work for IT/training code from Youtube/25. s.py'
path1 = path.replace('/', '\\') #замена слэша
print(path1)

r = path1.split('\\') #разбить по разделителю
##print(r)
print(r[-1])

##q = open('text5.txt', 'w', encoding='cp1251')
##q.write('У нас есть текст, который нужно\n\
##обработать. Убрать все (скобки), "ковычки",\n\
##и знаки переноса строки.')
##q = open('text5.txt', encoding='cp1251')
##print(q.read())

q = open('text6.txt', encoding='utf-8')
##print(q.read())
r1 = q.read()
list_znk = ['(',')','"','\n']#обработали текст
for i in list_znk:
    r1 = r1.replace(i, '')
print(r1)
r2 = r1.split()
print(r2)

new_text = ' '.join(r2)
print(new_text)

