f_name = "read.dat"
# TODO

with open(f_name,encoding='UTF-8') as f:
    AllDate=f.readlines()
    print(*AllDate[0],sep='')

"""
Number of males: _
Number of females: _
"""