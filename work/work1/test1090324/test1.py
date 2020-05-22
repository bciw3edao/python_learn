s={1,1,2}
print(s)

s.add(3)
#新增
print(s)

s.remove(2)
#刪除
print(s)

s.remove(3)
#修改:sets不再支援s[1]=99
#先移除在新增
print(s)

s.add(99)
print(s)
#查詢
print(99 in s)