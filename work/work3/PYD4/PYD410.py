# TODO
user_input = eval(input())
list_l = []
for x in range(user_input - 1):
    list_l.append(' ')
else:
    list_l.append('*')

    for star in list_l:
        print(star, end='')
    print()

for y in range(1, user_input):
    list_l[user_input - 1 - y] = '*'
    list_l.append('*')

    for star in list_l:
        print(star, end='')
    print()
