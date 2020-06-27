# TODO
user_input_1 = eval(input())
user_input_2 = eval(input())
num = 0
if user_input_1 % 2 != 0:
    user_input_1 += 1
for x in range(user_input_1, user_input_2 + 1, 2):
    num += x
print(num)
