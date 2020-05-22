def f(n):
    if n <= 3:
        return True
    else:
        return False


i = [5, 4, 3, 2, 1]
new_list = list(filter(f, i))
x=filter(f, i)
print(new_list)
print(x)
