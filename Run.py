from Children import *
from Housing import *

import os
os.system('clear')

print('MASH')
children = Children()
location = Location()
city = City()
woods = Woods()
beach = Beach()

print(f'You will have {children.value()} children')
print(f'You will live in the {location.value()}')

if location.value() == 'city':
    print(f'You will live in a {city.value()}')
elif location.value() == 'woods':
    print(f'You will live in a {woods.value()}')
elif location.value() == 'beach':
    print(f'Your will live in a {beach.value()}')




