import numpy as np

data = np.genfromtxt(r'..\data\elcand.csv', dtype=None, delimiter=',', encoding='UTF8',
                     names='c0,c1,c2,c3,c4,c5,c6,c7,c8,birthYear,c10,c11,c12,c13,elected,c15')

# print(data['birthYear'])
# age = 99 - data['birthYear']
# print(age)
# print(np.average(age))
# print(np.std(age))

# print(data['birthYear'][data['elected'] == '*'])
# age = 99 - data['birthYear'][data['elected'] == '*']
# print(age)
# print(np.average(age))
# print(np.std(age))

print(np.size(data, axis=0))
data = data[np.where(data['elected'] == '*')]
print(np.size(data, axis=0))
age = 99 - data['birthYear']
print(age)
print(np.average(age))
print(np.std(age))
# 會動到原始資料
