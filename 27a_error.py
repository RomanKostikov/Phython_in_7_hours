
##исправления ошибки без цикла
##enter = float(input('Введите число '))

##try:
##    enter = float(input('Введите число '))
##
##except ValueError:
##    print('Вы ввели не число!!!')
##    enter = float(input('Введите число '))
    

##исправление ошибки на постоянной основе с циклом 
##while True:
##    try:
##        enter = float(input('Введите число '))
##        break
##
##    except ValueError:
##        print('Вы ввели не число!!!')
##
##print('Все норм')

##исправления нескольких ошибок на постоянной основе
##while True:
##    try:
##        enter = float(input('Введите число '))
##        print(100/enter)
##        break
##
##    except ValueError:
##        print('Вы ввели не число!!!')
##
##    except ZeroDivisionError:
##        print('Делить на ноль нельзя!!!')
##
##print('Все норм')

##добавили доп оператор
##while True:
##    try:
##        enter = float(input('Введите число '))
##        print(100/enter)
##        
##    except ValueError:
##        print('Вы ввели не число!!!')
##
##    except ZeroDivisionError:
##        print('Делить на ноль нельзя!!!')
##    else:
##        print('Пользователь молодец, с первого раза!!!')
##print('Все норм')

##доп оператор finally(работает всегда)
while True:
    try:
        enter = float(input('Введите число '))
        print(100/enter)
        
    except ValueError:
        print('Вы ввели не число!!!')

    else:
        print('Пользователь молодец, с первого раза!!!')

    finally:
        print('Вывод финали')
print('Все норм')
