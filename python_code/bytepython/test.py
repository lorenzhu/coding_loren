'''
try:
    text = int(input("input a number: "))
    print(text/2)
except:
    print('error 999')
else:
    print("haha")
'''
def pass_tuple():
    return (2, 'error_details')

errum, errstr = pass_tuple()

print(errum, errstr)

a = 5; b = 10
a, b = b, a
print(a, b)