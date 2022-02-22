import numpy as np

a = np.arange(0, 27).reshape((3, 3, 3))

red = a[1,1,0:3]
blue = a[0:3,1,0]
green = a[0,0:3,2]

print(a, '\n',)
print('red', '\n', red)
print('blue', '\n', blue)
print('green', '\n', green)