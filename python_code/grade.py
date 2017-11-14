# _*_ coding: utf-8 _*_

'''
s1 = 72
s2 = 85
r = s1 / s2 * 100
print('grade increasing rate = %.1f %%' % r)

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
'''

'''
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))

print(classmates[0])
print(classmates[-1])

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)


L = ['Apple', 123, True]
print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s)


L = []
len(L)
'''


'''
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])

# 打印Python:
print(L[1][1])

# 打印Lisa:
print(L[2][2],'\n\n\n')

#list
classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates.pop()
print('classmates =', classmates, '\n\n\n')


#tuple
classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# cannot modify tuple:
#classmates[0] = 'Adam'
'''


'''
height = 1.75
weight = 80.5
'''
'''
height = float(input('身高(m)：'))
weight = float(input('体重(kg)：'))

bmi = weight / (height * height)

print('\n\nBMI = %.2f \n\n' % bmi)

if bmi >32:
	print('严重肥胖 bmi>32 ')
elif bmi > 28:
	print('肥胖 32>= bmi >28 ')
elif bmi > 25:
	print('过重 28>= bmi >25 ')
elif bmi > 18.5:
	print('正常 25>= bmi >18.5 ')
else:
	print('过轻 18.5>= bmi ')
'''


'''
#循环

sum = 0
#for x in [1,2,3,4,5,6,7,8,9,10]:
for x in range(101):
	sum = sum + x
print(sum)

sum = 0
n = 99
while n>0:
	sum = sum + n
	n = n - 2
print(sum,'\n\n\n')

L = ['Bart','Lisa','Adam']
for x in L:
	print(x)
'''

#dict
d = {'Micheal':95, 'Bob':75, 'Tracy':85}
print(d)

print(d['Micheal'])