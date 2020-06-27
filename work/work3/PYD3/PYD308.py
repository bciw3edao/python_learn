# TODO
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'#結束
    # 这并不能在所有操作系统上工作,可能會無效用，但不需要任何模块


user_input = eval(input())
for x in range(1, user_input + 1):
    user_input_num = eval(input())
    sun = 0
    for y in str(user_input_num):
        sun += int(y)
    print("Sum of all digits of %d is %d" % (user_input_num, sun))
    # print(color.BOLD + "Sum of all digits of %d is %d" % (user_input_num, sun) + color.END )

"""
Sum of all digits of _ is _
"""
