#!/usr/bin/env python3
#_*_  coding:utf-8  _*_

# Fibonacci series: 斐波那契数列
# 两个元素的总和确定了下一个数

a, b = 0, 1
while b<1000 :
    print(b, end=',')
    temp = b
    b = b + a
    a = temp
    #a, b = b, b + a
    
