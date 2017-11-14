# "ab"是地址(Address) 簿 (Book) 的缩写

ab = {
    'Swaroop'  :'swaroop@swaroopch.com',
    'Larry'    :'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer'  :'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Spammer'])

# 删除一对 key-value 对
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():  # 【.items()】
    print('Contact {} at {}'.format(name, address))

# 添加一堆 key-value 对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])