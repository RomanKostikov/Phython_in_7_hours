import os
##h = [9,8,7,4,5,6,3,2,1,5,5,-2]
##newh2 = [x*2 for x in h] #работа со списком
##z = {x*2 for x in h} #работа с множеством
##f = {x: x*2 for x in h} #работа со словарем
##g = [x for x in h if x % 2 == 0] #генератор с условием


g = [os.path.join(z, i)
     for z, x, c in os.walk('C:\\')
     for i in c if '.txt' in i]
print(g)
