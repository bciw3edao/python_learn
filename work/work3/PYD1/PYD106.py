x_min = float(input())
y_sec = float(input())
z_km = float(input())
# print((z_km / 1.6) / ((x_min * 60 + y_sec) / 3600))
print('Speed = %.1f' % ((z_km / 1.6) / ((x_min * 60 + y_sec) / 3600) ))
