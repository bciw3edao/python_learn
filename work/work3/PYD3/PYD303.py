# TODO
user_input = eval(input())
for x in range(1, user_input + 1):
    # print(x)
    for y in range(1, x + 1):
        # print(y)
        print('%4d' % (x * y), end='')
    print()
