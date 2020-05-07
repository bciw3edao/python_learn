l = [1, 'A']
print(l)
import numpy

arr = numpy.array([1, 'A'])
print(arr)
L = list(range(1, 5, 1))
print(L)
arr = numpy.arange(start=1, stop=5, step=.5)
print(arr)

# 列出元素型態
print(arr.dtype)
# 列出元素型態於記憶體之容量
# arr = arr.astype(numpy.int32)
print(arr.itemsize)
# 列出numpy 陣列於記憶體之容量(元素個數*元素型態容量)
print(arr.nbytes)

arr = arr.astype(numpy.int32)
print(arr.itemsize)
# 列出numpy 陣列於記憶體之容量(元素個數*元素型態容量)
print(arr.nbytes)
