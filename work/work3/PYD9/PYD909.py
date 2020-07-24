f_name = "data.dat"
# TODO
with open(f_name, 'w', encoding='utf-8') as f:
    for i in range(5):
        f.write(input())
        f.write('\n')
        i+=1

file = open(f_name)
print('The content of "data.dat":')
for txt in file.readlines():
    print(txt)
file.close()
"""
The content of "data.dat":
"""
