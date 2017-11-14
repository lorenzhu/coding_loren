import pickle

storefile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = open(storefile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(storefile, 'rb')
storedlist = pickle.load(f)
print(storedlist)