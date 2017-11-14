#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

age = int(input("请输入你家狗狗的年龄： "))
print("")

if age<0:
    print("r u kidding me?\n")
elif age == 1:
    print("相当于 14 岁的孩纸。\n")
elif age == 2:
    print("相当于 22 岁的年轻银。\n")
elif age > 2:
    human = 22 + (age-2)*5
    print("相当于 %d 的人。\n" % human)

### 推出提示
input("点击 enter 退出")
