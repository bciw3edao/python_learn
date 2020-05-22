import numpy as np
import time

startTime = time.time()
arr = np.arange(100_0000)
arr = np.where(arr % 2 == 0, arr + 1, arr - 1)
runTime = time.time() - startTime
print(runTime)


def mul(data):
    if data % 2 == 0:
        return data + 1
    else:
        return data - 1


startTime = time.time()
arr = np.arange(100_0000)
m_func = np.vectorize(mul)
arr = m_func(arr)
runTime1 = time.time() - startTime
print(runTime1)
