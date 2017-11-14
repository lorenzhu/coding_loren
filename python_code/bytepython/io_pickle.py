import pickle

# The name of the file where to store the object
storefile = 'shoplist.data'

# The list to store
shoplist = ['apple', 'mango', 'carrot']

# Write to the store_file
f = open(storefile, 'wb')
# Dump the object to the file
pickle.dump(shoplist, f)
f.close()

# Destroy the shoplist variable
del shoplist

# Read back from the storage
f = open(storefile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)