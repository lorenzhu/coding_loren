stop = int(input("输入截止数字："))

for num in range(2, stop+1):
    for i in range(2, num):
        if num % i == 0:
            print(num, '=', i, '*', num//i)
            break
    else:
        print(num, 'is prime')
