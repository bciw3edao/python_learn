# TODO
def compute(a, b, c):
    delta = ((b ** 2) - (4 * a * c))
    if delta > 0:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print(x1, ', ', x2, sep='')
    elif delta == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print('Your equation has no root.')


a = eval(input())
b = eval(input())
c = eval(input())
compute(a, b, c)
"""
Your equation has no root.
"""
