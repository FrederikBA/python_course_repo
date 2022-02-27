import numpy as np

data = np.arange(1,101).reshape(10,10)

even_numbers = data[data % 2 == 0]

ends_with_6 = data[np.where(data % 10 == 6)]

print(even_numbers)
print(ends_with_6)