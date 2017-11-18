from datetime import datetime

now = datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print('%s/%s/%s' % (now.year, now.month, now.day))
print("{}/{}/{}".format(now.year, now.month, now.day))
print("{}:{}:{}".format(now.hour, now.minute, now.second))

print("{}/{}/{} {}:{}:{}".format\
    (now.year, now.month, now.day, now.hour, now.minute, now.second))