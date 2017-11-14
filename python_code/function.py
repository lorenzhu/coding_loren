'''
print(abs(100))

print(abs(-100))

print(abs(12.34))

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x>=0:		 #缩进呀！！！
		return x
	else:
		return -x
		
		
import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
'''

'''
#计算一元二次方程的两个根	
import math

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

def quadratic(a,b,c):
	x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
	x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
	return x1, x2

print(quadratic(a,b,c))
'''

def power(x, n=2):
	s = 1
	while n>0:
		n = n-1
		s = s * x
	return s

def enroll(name, gender, age=6, city = 'Beijing'):
	print('names:', name)
	print('gender:', gender)
	print('age:', age)
	print('city', city)


def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
	
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

'''	
def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)
'''

	
	
def fact(n):
	return fact_iter(n, 1)
	
def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)
	
# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')