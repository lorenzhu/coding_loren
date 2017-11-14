#!/usr/bin/env python3
#_*_  coding:utf-8  _*_

# 猜数字游戏
number = 7
guess = -1
print("猜数字游戏！")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    
    if guess == number:
        print("恭喜你，猜对了\n")
    elif guess > number:
        print("猜的数字大了...\n")
    else:
        print("猜的数字小了...\n")
