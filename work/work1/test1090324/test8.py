dic = {1: 'mary', 2: 'jhon'}
key = int(input('input\nkey  :'))
'''if key in dic:
    print('value:', dic[key], sep='')
else:
    print('Not Exist')'''
print('value:', dic.get(key, 'Not Exist'), sep='')
