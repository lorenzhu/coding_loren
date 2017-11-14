points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]

print(points)

points.sort(key=lambda i: i['y'])

print(points)


'''列表推导'''
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)