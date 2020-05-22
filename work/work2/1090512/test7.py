import numpy as np

arr = np.arange(4)
print(arr)
print(arr.shape)
print(type(arr.shape))

row_vector = arr[np.newaxis, :]
print(row_vector)
print(row_vector.shape)

clumn_vector = arr[:, np.newaxis]
print(clumn_vector)
print(clumn_vector.shape)

arr = np.arange(1, 17).reshape(4, 4)
print(arr)
r = np.ravel(arr)
print(r)
print(r.shape)
