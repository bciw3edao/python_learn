import numpy as np

arr = np.array(['Michael', 'John', 'Mary', 'Tony', 'A123', 'B123', 'C123'])

fancy_index = np.where(np.char.startswith(arr, 'M'))
print(fancy_index)
print(arr[fancy_index])
