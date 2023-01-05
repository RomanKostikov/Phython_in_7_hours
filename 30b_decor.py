def decor(f):
    def wrapper(): #wrapper = перевод обертка
        try:
            h = f()
        except Exception:
            print('Повторите ввод...')
            h = f()
        return h
    return wrapper

@decor # make = decor(make)
def make():
    enter = float(input('Введите число: '))
    return enter
@decor
def make2():
    enter = float(input('Введите число опять: '))
    return enter

make2()
make()
