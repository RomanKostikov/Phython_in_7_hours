price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

for i in price:
    price[i] = round(price[i] * 0.85, 2)

print(price)
