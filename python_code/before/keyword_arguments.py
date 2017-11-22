def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)                                          # 1 positional argument
print()
parrot(voltage=1000)                                  # 1 keyword argument
print()
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
print()
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
print()
parrot('a million1', 'bereft of life2', 'jump3')         # 3 positional arguments
print()
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
# Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
# Arguments: spam eggs
# 'spam and eggs'
