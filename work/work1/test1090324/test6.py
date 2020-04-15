dic = {1: 'mary'}
print(type(dic))
print(dic)
# add
dic[2] = 'jhon'
# key重覆會覆蓋
dic[1] = 'david'
print(dic)
# 刪除
del dic[2]
print(dic)
# 修改
dic[1] = 'jhon'
print(dic)
dic.update({1: 'jhon chon'})
# 查詢
print(1 in dic)
