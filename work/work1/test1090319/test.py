fraction = 0
l = list()
while True:
    fraction = int(input('請輸入分數:'))
    if fraction <= -1: break
    l.append(fraction)
    #l +=[fraction]

print('分數清單:', l)
average = sum(l) / len(l)
print('平均    :', average)
print('最高分數:', max(l))
