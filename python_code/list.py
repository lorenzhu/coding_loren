
list1 = ['Google', 'Baidu', 1997, 2000];
print('list1 =', list1)

list2 = list(range(1,8));
print('list2 =', list2)

print('list1[0] =', list1[0])
print('list1[0] = %s' %(list1[0]))

print('list2[1:5] =', list2[1:5])

print('list1第三个元素为： ', list1[3])
list2[2] = 2001
print('更新后为： ',list1[3])

del list1[2]
print('删除第三个元素后：', list1)

print('len(list1) = ', len(list1))

print('list1 + list2 =', list1 + list2)

print('list1*4 : ', list1*4)

print('1997 in list1: ', 1997 in list1)

for x in list1:
    print(x, end='\n')

list2[len(list2)-1] = list1
print(list2)


list3 = list(range(1,11))
print('max(list3) = ', max(list3))
print('min(list3) = ', min(list3))

list4 = list({9,0,8,11})
print(list4)
list4.append(1111)
print(list4)

list01 = [444, 333, 222]
list01.append(111)
print ("更新后的列表 : ", list01)
list01.remove(333)
print ("更新后的列表 : ", list01)
