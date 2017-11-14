import random

answer = random.randint(1,10)

print('...........我爱 SYSU ............')

for n in list(range(3)):
    temp = input('哥们，猜猜我在想的数字吧: ')
    guess = int(temp)
    if guess == answer:
        print('卧槽，你是哥心里的蛔虫吗？！')
        print('So what？猜中也没有奖励')
        break
    else:
        if guess > answer:
            print('哥，大了大了---')
        else:
            print('哥，小了小了')


print('其实答案是：%d' % answer)
print('Game over, 不玩了^_^')
