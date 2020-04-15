f = open(r'/work1/text/text1.txt')
x = f.read()
print(type(x))
print(x)
print(len(x))
f.close()

f = open(r'/work1/text/text1.txt')
while True:
    date = f.readline()
    if not date:
        break
    print(date)
print('close?', f.closed)
f.close()
print('close?', f.closed)

# f = open(r'D:\程式\python\work\text\text1.txt')
with open(r'/work1/text/text1.txt') as f:
    all = f.readlines()
    print(type(all))
    for x in all:
        print(x, sep='', end='\n')
    # f.close()
    print('close?', f.closed)
print('close?', f.closed)
f.close()
