n = list(range(1, 21))
m = []

for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)
        

else:
    print(n)
    print(m)
