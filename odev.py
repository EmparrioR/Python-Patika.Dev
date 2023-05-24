# 1. Soru 

import numpy as np

np_list = np.array([1,'a','cat',2,3,'dog',4,5]);

flattened = np_list.flatten();

print(flattened);

# 2. Soru

list_2 = [[1, 2], [3, 4], [5, 6, 7]]

# Burada liste içindeki alt listeleri ters çevirdik
list_2_reversed = [sublist[::-1] for sublist in list_2]

# Burada ise listeyi ters çevirdik
list_2_reversed.reverse();

print(list_2_reversed);