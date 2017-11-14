bri = set(['brazil', 'russia', 'india'])

print('bri:', bri)
print('india in bri:', 'india' in bri)
print('usa in bri:', 'usa' in bri)

bric = bri.copy()
print('bric:', bric)

bric.add('china')
print('bric:', bric)

print('bric.issuperset(bir):', bric.issuperset(bri))

bri.remove('russia')
print('\nbri&bric', bri&bric)
print('bri.intersection(bric):', bri.intersection(bric))