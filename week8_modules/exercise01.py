from cv2 import detail_DpSeamFinder
import numpy as np
import pandas as pd

data = {'Height':[55, 47, 42, 70, 51, 53], 'Weight':[3.0, 2.8, 3.5, 2.9, 2.7, 3.2], 'Age':[3, 4, 8, 6, 5, 9]}
df = pd.DataFrame(data)

dd = df.to_numpy()



def generate_babies(amount):
  baby_list = []
  while amount > 0:
    baby_list.append((np.random.randint(42, 56), round(np.random.uniform(2.4, 3.8),1) , np.random.randint(2, 12)))
    amount -= 1
  
  return np.asarray(baby_list)

print(generate_babies(5))