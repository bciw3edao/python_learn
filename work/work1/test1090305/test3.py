a = int(input('InputSomeshingNumber(a)'))
b = int(input('InputSomeshingNumber(b)'))
c = int(input('ChooseStyle(1~4)'))
if c == 1:
    print("Style(1):%d+%d=%d" % (a, b, a + b))
elif c == 2:
    print('Style(2):{0}+{1}={2}'.format(a, b, a + b))
elif c == 3:
    print(f"Style(3):{a}+{b}={a + b}")
elif c == 4:
    print('Style(1):',a, '+', b, '=', a + b, sep='')
else:
    print('Style_Choose_error')
