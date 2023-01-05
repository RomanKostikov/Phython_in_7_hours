d1 = {'a': 7}
d2 = dict(a=7)
d3 = dict.fromkeys([1,2,3,4,5], 'value')

price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water':0.2}

def buy():
    pay = 0
    while True:
        enter = input('Что покупаем???\n')
        if enter == 'end':
            break
        pay += price[enter]
    return pay
