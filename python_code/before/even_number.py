stop = int(input("输入截止数字："))

for num in range(2, stop+1):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
