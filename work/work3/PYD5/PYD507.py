# TODO
user_input = eval(input())


def compute(user_input):
    if user_input >= 0:
        num_range = range(1, user_input + 1, 1)
    else:
        num_range = range(-1, user_input - 1, -1)
    check = 0
    for i in num_range:
        if user_input % i == 0:
            check += 1
    if check == 2:
        return True
    else:
        return False


if compute(user_input):
    print("Prime")
else:
    print("Not Prime")

"""
Prime
Not Prime
"""
