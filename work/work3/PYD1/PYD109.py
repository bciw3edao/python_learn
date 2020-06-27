import math

s = float(input())
Regular_pentagon = (5 * s ** 2) / (4 * math.tan(math.pi / 5))
print('Area = %.4f' % Regular_pentagon)
