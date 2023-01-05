price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

new_price = {}
for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 2)

print(new_price)
##new = {}
##for key, value in price.items():
##    new[value] = key
##print(new)

for value in price.values():
    print(value)
