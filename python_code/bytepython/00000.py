'''
phrase = "A bird in the hand ..."

for char in phrase:
    if char =='A' or char =='a':
        print("X", end=' ')
    else:
        print(char, end=' ')
'''

choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
  print(index+1, item)

# for...else...
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!') # (It actually is.)
    break
  print('A', f)
else:
  print('A fine selection of fruits!')