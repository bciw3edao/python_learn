import numpy as np


def filter(data, key):
    if data == key:
        return data


arr = np.array(['Michael', 'John', 'Mary', 'Tony', 'A123', 'B123', 'C123'])
key = input('請輸入名字字首(大寫)')
i = 0
for str in arr:
    if str[0] == key:
        print(str)
        i+=1
else:
    print('Notfind\n'if i==0 else '',end='')

# print(arr[arr >= key] if arr[arr >= key].size != 0 else 'NotFind')
