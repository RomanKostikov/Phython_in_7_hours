import time

def f(*args):
    list_new = []
    for i in args:
        for y in i:
            if y not in list_new:
                list_new.append(y)
        return list_new
z = list(range(10000))
x = list(range(5000, 15000))
c = list(range(10000, 20000))

start = time.time()
f(z,x,c)
stop = time.time() - start
print(stop)

start2 = time.time()
r = set(z)
t = r.union(set(x), set(c))
stop2 = time.time() - start2
print(stop2)
