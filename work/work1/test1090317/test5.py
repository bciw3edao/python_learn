l = list(range(0, 10))
print(l)
for x in range(len(l)):
    l[x] = l[x] ** 2
print(l)
l = list(range(0, 10))
for idx, value in enumerate(l):
    l[idx] = value ** 2
print(l)
# new_list=[expression for_loop conditions]
l = list(range(0, 10))
l = [x ** 2 for x in l]
print(l)
l = list(range(0, 10))
l = [x ** 2 for x in l if x < 5]
print(l)
l = list(range(0, 10))
l = [x ** 2 if x < 5 else x for x in l]
print(l)
