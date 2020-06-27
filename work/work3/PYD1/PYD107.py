list_num = []
for x in range(5):
    num = eval(input())
    list_num.append(num)
print(*list_num)
print('Sum = %.1f' % (sum(list_num)))
print('Average = %.1f' % (sum(list_num) / len(list_num)))
