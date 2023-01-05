def decor(f):
    def wrapper(): #добавили функцию обертку
        print('Код декоратора')
        f()
        print('Второй код декоратора')
    return wrapper

@decor # make = decor(make)
def make():
    enter = input('Enter something... ')
    print(enter)

print('здесь')
make()
##h = make
##h()
