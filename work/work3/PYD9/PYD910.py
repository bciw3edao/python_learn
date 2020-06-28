f_name = "read.dat"
# TODO
import numpy as np

# npdate=np.genfromtxt('read.dat',encoding='UTF-8',delimiter=' ',dtype=str)
# print(npdate)
with open(f_name, encoding='UTF-8') as f:
    AllDate = f.readlines()
    AllDateNp = np.array(None, dtype=str)

    for date in AllDate:
        if date != None:
            print(date)
        AllDateNp = np.append(AllDateNp, values=date.split(' '))

    AllDateNp = np.delete(AllDateNp, obj=[0])
    AllDateNp.shape = (int(len(AllDateNp) / 4), 4)

males = 0
females = 0
for date in AllDateNp:
    if date[2] == '性別':
        continue
    elif int(date[2]) == 0:
        females += 1
    else:
        males += 1
print('Number of males: %d' % males)
print('Number of females: %d' % females)

"""
Number of males: _
Number of females: _
"""
