import numpy as np

# 建立一個2*3的陣列,初始值為0
arr = np.zeros(shape=(2, 3))
print(arr)
# 新增橫列(ROW)至最後
arr = np.append(arr, values=[[1, 2, 3]], axis=0)
print(arr)
# 新增橫列(ROW)至指定位置
arr = np.insert(arr, obj=[0], values=[4, 5, 6], axis=0)
print(arr)

# 新增直欄(Column)至最後
arr = np.append(arr,values=[[1],[2],[0],[0]],axis=1)
print(arr)
# 新增直欄(Column)至指定位置
arr = np.insert(arr,obj=[0],values=[[98],[99],[0],[0]], axis=1)
print(arr)
# delete指定橫列(ROW)
arr = np.delete(arr,obj=[1,3],axis=0)
print(arr)