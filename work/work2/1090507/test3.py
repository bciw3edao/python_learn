import numpy as np

arr = np.arange(1, 51)
mask = (arr <= 10) | (arr >= 44)
print(mask, type(mask))
print(arr[mask])
