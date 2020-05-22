import numpy as np
import time

startTime = time.time()
arr = np.arange(1_000_0000)
arr = arr * 2
endTime = time.time() - startTime
print(endTime)

startTime = time.time()
arr = np.arange(1_000_0000)
for index, x in np.ndenumerate(arr):
    arr[index] = x * 2
endTime1 = time.time() - startTime
print(endTime1)
print(endTime1 / endTime)
