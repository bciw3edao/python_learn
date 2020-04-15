s1 = set('michael')
print(s1)
s2 = set('michelle')
print(s2)
intersect = s1 & s2
print(len(intersect))
union = s1 | s2
print(len(union))
print('jaccard similarity:', round(len(intersect) / len(union) * 100, 2), '%', sep='')
