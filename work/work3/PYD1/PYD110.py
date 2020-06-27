import math

n_side = float(input())
s_Side_length = float(input())
Regular_pentagon = (n_side * math.pow(s_Side_length, 2)) / (4 * math.tan(math.pi / n_side))
print('Area = %.4f' % Regular_pentagon)
