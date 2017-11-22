def pwd_input(msg = ''):  
    import msvcrt, sys  
  
    if msg != '':  
        sys.stdout.write(msg)  
    chars = []  
    while True:  
        newChar = msvcrt.getch()  
        if newChar in '\3\r\n': # 如果是换行，Ctrl+C，则输入结束  
            print ('')  
            if newChar in '\3': # 如果是Ctrl+C，则将输入清空，返回空字符串  
                chars = []  
            break  
        elif newChar == '\b': # 如果是退格，则删除末尾一位  
            if chars:  
                del chars[-1]  
                sys.stdout.write('\b \b') # 左移一位，用空格抹掉星号，再退格  
        else:  
            chars.append(newChar)  
            sys.stdout.write('*') # 显示为星号  
    return ''.join(chars)


pwd_input()
