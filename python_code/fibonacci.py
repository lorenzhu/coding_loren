def fib(n):
    a, b = 0, 1
    while b <= n:
        print(b, end=', ')
        a, b = b, b+a
    print()

def fib2(n):
    result = []
    a = 0
    b = 1
    while b <= n:
        result.append(b)
        temp = a
        a = b
        b = b + temp
    return result

print("斐波那契数列1")
stop1 = int(input('输入截止数字：'))
fib(stop1)

print()

print("斐波那契数列2")
stop2 = int(input('输入截止数字：'))
print(fib2(stop2))


        
