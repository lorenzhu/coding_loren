# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供
 
# 导入 cmath(复杂数学运算) 模块
import cmath
 
a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))
 
# 计算
d = (b**2) - (4*a*c)
 
# 两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
 
print('结果为 {0} 和 {1}'.format(sol1,sol2))



'''
#考虑到了无穷解与无解的情况
import math

a,b,c = input("请输入3个数字(空格分隔)：").split()
a = float(a)
b = float(b)
c = float(c)
d = (b**2) - (4*a*c)
if a==0 and b==0 and c==0 :
  print("有无穷个解")
elif d >= 0:
  x1 = (-b-d/(2*a))
  x2 = (-b+d/(2*a))
  print('结果为：%.2f,%.2f'%(x1,x2));
else:
  print("无解")
'''


select websites.name, access_log.count, access_log.date
from websites left join access_log
on websites.id=access_log.site_id
order by access_log.count desc;

select websites.name, access_log.count, access_log.date
from access_log
right join Websites
on Websites.id=access_log.site_id
order by access_log.count desc;
