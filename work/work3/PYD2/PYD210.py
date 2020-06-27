side1 = eval(input())
side2 = eval(input())
side3 = eval(input())

# TODO
if side1 >= (side2 + side3):
    print('Invalid')
elif side2 >= (side1 + side3):
    print('Invalid')
elif side3 >= (side1 + side2):
    print('Invalid')
else:
    print(side1+side2+side3)


"""
Invalid
"""
