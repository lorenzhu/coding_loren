#!/usr/bin/env python3

import sys; x = 'loren'; sys.stdout.write(x + '\n')

x="a"
y="b"
# 换行输出
print( x )
print( y )

print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()

# 导入 sys 模块
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
	print(i)
print('\n python 路径为', sys.path, '\n\n')

# 导入 sys 模块的argv, path成员
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path