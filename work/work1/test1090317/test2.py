x = [1, 3, 2]
for a in x:  # 標頭搜尋
    print(a, end=',')
print()
for i in range(len(x)):  # 所引搜尋
    print(x[i], end=',')
print()
for idx, value in enumerate(x):  # 函式雙回傳
    print('[', idx, ']=', value, sep='')
