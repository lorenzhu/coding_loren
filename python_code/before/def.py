# 函数
def hello():
    print("Hello World!")

hello();

# 计算面积函数
def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

print_welcome("Loren")
w = 4
h = 5
print("width =", w, "height =", h, "area =", area(w, h), "\n\n")

# 函数调用
# 定义函数
def printme( str ):
    "打印任何传入的字符串"
    print(str);
    return;  # None

# 调用函数
printme("我要调用用户自定义函数！");
printme("再次调用同一函数");
printme("\n\n")


# 传递不可变对象
def ChangeInt( a ):
    a = 10
    print("函数内：", a)
    
b = 2
ChangeInt( b )
print( "函数外：", b )  #2
print("\n\n")

# 传递可变对象
def changeme( mylist ):
    mylist.append([1,2,3,4])
    print("函数内取值：", mylist)
    #return

mylist = [10, 20, 30];
changeme( mylist );
print("函数外取值：", mylist, "\n")


"1必需参数"
#printme()
"2关键字参数"
printme(str="runoob")

"3默认参数"

"4不定长参数"
def printinfo( arg1, *vartuple):
    print( arg1, "\n" )
    for var in vartuple: print( var ); print("haha")
    return;

printinfo( 10 );
printinfo( 10, 222, 333, '\n' );

# 匿名函数
mysum = lambda arg1, arg2: arg1 + arg2;
print("sum(10, 20):", mysum(10, 20))

if True:
    msg = "I am Loren"

print(msg)
