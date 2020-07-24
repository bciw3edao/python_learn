# TODO
user_input = eval(input())


def compute(user_input):
    num1 = 0
    num2 = 1
    print(num1, num2, end=' ')
    for x in range(user_input - 2):
        if x % 2 == 0:
            num1 += num2
            print(num1, end=' ')
        else:
            num2 += num1
            print(num2, end=' ')


if user_input >= 2:
    compute(user_input)
