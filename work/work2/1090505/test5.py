import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr[0])
print(arr[[0, 2, 4]])
# Mask index
a=1
print(arr[[True, False, True, False,True if a!=0 else False]])
