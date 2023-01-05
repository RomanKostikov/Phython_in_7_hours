import os
h = [9,8,7,4,5,6,3,2,1,5,5,-2]
##newh2 = [x*2 for x in h] #генератор списка
##z = {x*2 for x in h} #генератор множества
##f = {x: x*2 for x in h} #генератор словаря
##g = [x for x in h if x % 2 == 0] #генератор с условием


price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}
#без генератора
new_price = {}
for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 2)
print(new_price)
#с генератором
new_d = {i: round(price[i] * 0.85, 2) for i in price.keys()}
print(new_d)

z = (x*2 for x in h) #выражение генератора, не путать!
