user_input = input()
if user_input.isalpha():
    print('%s is an alphabet.' % user_input)
elif user_input.isdigit():
    print('%s is a number.' % user_input)
elif user_input.isascii():
    print('%s is a symbol.' % user_input)
