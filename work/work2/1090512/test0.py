import numpy as np

arr = np.array(['Michael', 'John', 'Mary', 'Tony', 'A123', 'B123', 'C123'])


def start_with(data, char):
    return data.startswith(char)


s_with = np.vectorize(start_with)
print(s_with(arr, 'M'))
print(arr[s_with(arr, 'M')])
