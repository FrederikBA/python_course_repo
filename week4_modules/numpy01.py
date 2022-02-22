import numpy as np

a = np.arange(10,30).reshape(4,5)

yellow = a[0,0]
teal = a[:,1:4:2]
red = a[0,1:4]
blue = a[0:4:2,4]
green = a[0:3,2]

print(a)
print(yellow)
print(teal)
print(red)
print(blue)
print(green)

