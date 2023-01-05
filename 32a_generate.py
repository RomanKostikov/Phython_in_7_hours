h = ['https:\\www.сайт.com', 'https:\\www.какойтосайт.net',
     'https:\\www.левыйсайт.com', 'https:\\www.другойсайт.com',
     'https:\\www.сайтишка.net', 'https:\\www.сайтец.com']

##n = [x.split('\\')[1] for x in h if '.com' in x] #генератор списка
##print(type(n)) #для определения различия(<class 'list'>)

z = (x.split('\\')[1] for x in h if '.com' in x) #выражение генератора
##print(type(z)) #<class 'generator'>

for i in z: #разница от генератора списка, выгружает последовательно каждое значение 
    print(i)
n = [x.split('\\')[1] for x in h if '.com' in x]

z = (x.split('\\')[1] for x in h if '.com' in x)
