s = {0}
print(type(s))
dic = {1: 'mary', 2: 'jhon'}
x = {}
print(type(x))
print(dic[1])
key = int(input('input\nkey  :'))
if key in dic:
    print('value:', dic[key], sep='')
else:
    print('Not Exist')
