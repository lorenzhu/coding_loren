# 这是一个字符串对象
name = "LorenZhu"

if name.startswith("Lor"):
    print('Yes, the string starts with "Lor"')

if 'Z' in name:
    print('"Z" is in the string')

if name.endswith("Zhu"):
    print('Yes, the string ends with "Zhu"')

if name.find("ren") != -1:
    print('Yes, it contains the strong "ren"')

delimeter = '_*_'
bric = ['brazil', 'russia', 'india', 'china']
print(delimeter.join(bric))


