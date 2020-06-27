import numpy as np
from scipy.spatial.distance import pdist

x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
print('(', x1, ',', y1, ')')
print('(', x2, ',', y2, ')')
X = np.vstack([[x1, y1], [x2, y2]])  # 將x,y兩個一維數組合併成一個2D陣列 ；[[x1,x2,x3...],[y1,y2,y3...]]
Distance = pdist(X)  # 兩座標的歐式距離，輸出到小數點後第4位
print('Distance = %.4f' % Distance)
