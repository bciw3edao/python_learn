# TODO
user_input = eval(input())
total = 0
for x in range(2, user_input + 1):
    total += 1 / ((x - 1) ** 0.5 + x ** 0.5)
print('%.4f'%total)
