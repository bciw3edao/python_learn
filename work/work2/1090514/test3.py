import numpy as np

arr = np.array([range(1, 4), range(4, 7)])
print(arr)
for x in np.nditer(arr):
    print(x)

for index, x in np.ndenumerate(arr):
    print(index, type(index))
    print(x, type(x))
