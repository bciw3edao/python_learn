try:
    print('step:1')
    print(1 / 0)
    print('step:2')
except:
    print('exception:1')
    import sys

    exception = sys.exc_info()
    print(type(exception))
    print(exception)
else:
    print('??????????????')
finally:
    print('ok')
print('---------------')
