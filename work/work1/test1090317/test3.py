i = [5, 4, 3, 2, 1]
new_list = []
x_list = []
y_list = []
for x in i:
    if x <= 3:
        new_list.append(x)
        x_list = [*x_list, x]
        y_list += [x]

print(new_list)
print(x_list)
print(y_list)
