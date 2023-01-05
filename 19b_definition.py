import math

PI = math.pi

def radius():
    n = float(input('Диаметр цилиндра в см: '))
    n /= 2
    return n
def height():
    m = float(input('Высота цилиндра в см: '))
    return m
def volume():
    r = radius()
    h = height()
    s = PI*r**2
    v = s*h

    return v
print('Объем цилиндра', volume(), 'см3')

def massa(g):
    n = float(input('Удельный вес г/см3: '))
    return g*n/1000
print('Вес цилиндра в кг: ', massa(volume()))
