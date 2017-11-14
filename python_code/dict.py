#!/usr/bin/env python3
#_*_   coding:utf-8  _*_
'''
dorm518 = {'xwg':'00000000', 'zly':'13342113', 'zcp':'13342110', 'zqh':'13342112', 'zxq':'13342111'}

print(dorm518['zly'])
print(dorm518['zqh'])

#print(dorm518['luojun'])

dorm518['zly'] = '17215198'
print(dorm518['zly'])

print(dorm518['xwg'])
del dorm518['xwg']

print(str(dorm518))
print(str(dorm518))
print(str(dorm518))
      
print(type(dorm518))

member =('zly','zxq','zqh','zcp')
number = (1,2,3,4)
dorm518 = dorm518.fromkeys(member, 10)
print(dorm518)

print(dorm518.items())
dorm518n = {'ggg':'666'}
dorm518.update(drom518n)
print(dorm518)
'''

dorm518 = {'xwg':'00000000', 'zly':'13342113', 'zcp':'13342110', 'zqh':'13342112', 'zxq':'13342111'}
dorm518new = {'zly':'17215198'}
dorm518.update(dorm518new)
print(dorm518)
