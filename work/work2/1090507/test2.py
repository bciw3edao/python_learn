import numpy as np

arr = np.arange(1, 11)
print(arr)
print(arr < 5)

t = np.where(arr < 5)
print(t)
print(type(t))
print(arr[t] ** 2)
