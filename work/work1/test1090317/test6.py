def power(i):
    return i ** 2


l = list(range(0, 10))
m = map(power, l)
newL = list(m)
print(newL)
l = list(range(0, 10))
m = map(lambda p: p ** 2, l)
newL = list(m)
print(newL)
