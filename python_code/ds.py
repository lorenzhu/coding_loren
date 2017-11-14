
a = [66.25, 333, 333, 1, 1234.5]
print(a)
print(a.count(333), a.count(66.25), a.count('x'))

matrix = [
             [1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
            ]

print(matrix)

matrixT = [[row[i] for row in matrix] for i in range(4)]
print(matrixT)


transposed = []
for i in range(4):
     transposed.append([row[i] for row in matrix])
     
print(transposed)
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


transposed = []
for i in range(4):
     # the following 3 lines implement the nested listcomp
     transposed_row = []
     for row in matrix:
         transposed_row.append(row[i])
     transposed.append(transposed_row)

print(transposed)

t = 12345, 54321, 'hello!'
tuple0 = t, (1,2,3,4,5)
print(tuple0)
print(tuple0[0][1],'\n\n\n')

# =====================集合======================= 
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('\'orange\' in basket: ', 'orange' in basket )
print('\'crabgrass\' in basket: ', 'crabgrass' in basket)


a = set('abracadabra')
b = set('alacazam')
print(a,'\n',b,'\n\n\n')

#====================字典============================
tele={'jack':1111, 'sape':2222}
print(tele)
tele['guido'] = 3333
print(tele)
print(list(tele.keys()))
print(list(tele.values()))
print(sorted(tele.keys()))
'guido' in tele

