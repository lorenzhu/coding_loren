# 用户输入数字
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')

# 求和
sum12 = float(num1) + float(num2)

# 显式计算结果
print('数字 {0} 和 {1} 相加结果为： {2} '.format(num1, num2, sum12))
print('数字 %.2f 和 %.2f 相加结果为： %.2f ' % (float(num1), float(num2), sum12))


print('\r\n\r\n一行代码')

print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))
