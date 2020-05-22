import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr)
print(arr[:2, :2])
print(arr[0, 0])

print(arr.ndim, '個維度')
print(arr.shape, '個元素')
print('type', arr.dtype)
print('共', arr.size, '個')
