# TODO
k = int(input())

if k not in range(1, 100):
    print("Please input 1~100 digital")
else:
    for i in range(k):
        num_lst = input().split(' ')
        list_a =list(map(float, num_lst[0:]))
        print("%.2f" % (max(list_a) - min(list_a)))
