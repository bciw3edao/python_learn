import numpy as np

arr = np.array([4, 2, 1, 3])
print(np.sort(arr))
print(arr)
print(np.argsort(arr))
print(arr[np.argsort(arr)])
print(np.sort(-arr))
print(-np.sort(-arr))
print(arr)
print('___________________________________________')
arr = np.array(['Michael', 'Mary'])
lenFunction = np.vectorize(len)
print(lenFunction(arr))
print('___________________________________________')


def m_len(data):
    print(data)
    return len(data)


lenFunction = np.vectorize(m_len)
print(lenFunction(arr))