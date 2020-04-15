t = (1, 2, 3, 4)
for x in t:
    print(x)
a, b, *c = t
print(a, b, c)
print(type(c))
