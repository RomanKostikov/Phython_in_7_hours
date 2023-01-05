x = [1, 2]

if x == 0:
    x = 1
    print('х был равен нулю')

elif type(x) == type(5) or type(x) == type(5.5):
    print('x допустимое значение')

else:
    print('В х не допустимый тип данных')
    x = 1

print(100/x)
