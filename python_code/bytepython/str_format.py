age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book\n'.format(name, age))
print('Why is {0} playing with that python?\n'.format(name))


print('{0:.3f} \n'.format(1.0/3))  # 对于浮点数 '0.333' 保留小数点(.)后三位
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11} \n'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book} \n'.format(name='Swaroop', book='A Byte of Python'))

s01 = 'this is string \
    and still string'

print(s01,'\n')

s02 = r"Newlines are indicated by \n"
print(s02)

print(2<<2)
print(32>>2)