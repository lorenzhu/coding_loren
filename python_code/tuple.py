# tuple
tup1 = ('Google', 'Runoob', 1997, 2000);
tup2 = tuple(range(1,6))
tup3 = 'a','b','c','d';
print(tup1,'\n',tup2,'\n',tup3)


tup4 = ()
print(tup4)

tup5 = (50)
print(type(tup5))
tup6 = (50,)
print(type(tup6))

print('tup1[0] = ',tup1[0])
print('tup2[1:5] =', tup2[1:5])

tup11 = (12, 34.56)
print(tup11)
tup22 = ('abc', 'xyz')
print(tup22)

tup33 = tup11 + tup22
print(tup33)

#print(tup33)

print('marker--------------')


tupp = tuple(range(1,11))
print(tupp)
listt = list(tupp)
print(listt)
tupp2 = tuple(listt)
print(tupp2)
