import numpy as np

dtype = [('id', int), ('name', 'S5')]
data = [(1, 'Mary'), (2, 'Jhon')]
arr = np.array(object=data, dtype=dtype)
print(arr)
# mask = (arr['id'] == 1) & (arr['name'] == 'Mary'.encode())
# print(arr[mask])
print(np.sort(arr, order='name'))
print(np.sort(arr, order='id'))
