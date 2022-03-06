import numpy as np
import pandas as pd

data = np.array(
    [
        ["", "Col1", "Col2", "col3"],
        ["Row1", 1, 2, 3],
        ["Row2", 4, 5, 6],
        ["Row3", 7, 8, 9],
    ]
)

dd = pd.DataFrame(data=data[1:4, 1:4], columns=data[0, 1:4], index=data[1:4, 0])

red = dd["Col2"]
green = dd.iloc[:, 2]
blue = dd.iloc[2, 1]


print(dd, "\n")
print(red, "\n")
print(green, "\n")
print(blue, "\n")
