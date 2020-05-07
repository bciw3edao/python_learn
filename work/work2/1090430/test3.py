a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(type(c))
print(c)

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(type(c))
print(c)
print(a ** 2)

import time

l = list(range(100_0000))
starttime = time.time()
# print(l)
l = [x ** 20 for x in l]
# print(l)
listRunTime = time.time() - starttime
print('listRunTime=', listRunTime)

starttime = 0

arr = np.arange(100_0000)
starttime = time.time()
# print(arr)
arr = arr ** 20000
# print(arr)
npRunTime = time.time() - starttime
print('npRunTime=', time.time(), '-', starttime, '=', npRunTime)
print('效能差異:', listRunTime / npRunTime)
