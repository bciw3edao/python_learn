import csv

with open(r'..\txt\aa.txt') as f:
    data1 = csv.reader(f)
    next(data1)
    for y in data1:
        print(y)
    f.seek(0)  # 移動標頭
    data = csv.reader(f)
    print(type(data))
    for x in list(data)[1:]:
        print(x, type(x))
        print(x[1], len(x[1]))
    f.seek(0)
    data2 = csv.DictReader(f)
    for z in data2:
        print(z['id'], x['name'])
