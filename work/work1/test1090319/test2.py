m = 6
l = list(range(m))
l.remove(0)

int_n = int(input('input number(1~5)'))
print(l[:int_n])
print(l[int_n * -1:])
print('---------')

x = 1
while x <= int_n:
    print(l[-x], end=' ')
    x += 1

print('\n---------')

print(l[-1:-1 - int_n:-1])

i = l[-int_n:]
i.reverse()
print(i)
