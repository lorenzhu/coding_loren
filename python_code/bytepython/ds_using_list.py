# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print("I have", len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shoppint list is now', shoplist, '\n')

print('I will sort my  list now')
shoplist.sort()
print('Sorted shopping list is', shoplist, '\n')

print('The first item I will buy is', shoplist[0], '\n')
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist, '\n')