import numpy as np

arr = np.array([1, 2, 3], dtype=np.uint8)
# uint8=>2^8=0~255
arr = arr.astype(np.int32)
# int32=>2^32=4,294,967,296
arr = arr + 255
print(arr)
