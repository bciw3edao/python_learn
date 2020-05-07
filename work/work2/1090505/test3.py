import numpy as np

arr = np.array([1, 2, 3])
print(arr)
# 新增至最後
arr = np.append(arr, 4)
print(arr)
# 新增至指定位置
arr = np.insert(arr, obj=[0], values=[5])
print(arr)
