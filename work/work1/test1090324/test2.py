a = {1, 2}
b = {2, 3}
# 交集
print(a.intersection(b))
# 聯集
print(a.union(b))
c = {*a, *b}
print(c)
# 差集
print(a.difference(b))
print(a - b)
