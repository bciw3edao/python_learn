import numpy as np

# arr = np.arange(3)
# print(arr)
# arr += 5
# print(arr)

# arr = np.ones(shape=(3, 3))
# print(arr)
# arr1 = np.arange(3)
# print(arr1)
# arr = arr + arr1
# print(arr)

# arr = np.arange(3)[:, np.newaxis]
# print(arr, arr.shape)
# arr1 = np.arange(3)
# print(arr1, arr1.shape)
# arr = arr + arr1
# print(arr)

# arr = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30]])
# print(arr)
# arr1 = np.arange(4)[:, np.newaxis]
# print(arr1)
# arr = arr + arr1
# print(arr)

a = np.array([[2, 1, 4, 5], [1, 2, 1, 8], [5, 3, 3, 7], [5, 1, 6, 5]])
b = np.array([4, 5, 2, 7])
print(np.linalg.solve(a, b))
