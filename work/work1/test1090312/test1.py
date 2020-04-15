def add_all(*args):
    print(type(args))
    return sum(args)


print(add_all(10, 20, 30))
print(add_all(10))
