l=[1,2,3]
def mul (element):
    return element*2

l =map(mul,l)
print(l)
for x in l:
    print(x)
import numpy as np
arr=np.array(['Michael','Mary'])
lenFunction = np.vectorize(len)
print(lenFunction(arr))