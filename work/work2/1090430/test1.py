# import math
# print(math.sqrt(4))
import csv

with open(r'..\voteData\2010村里長\elcand.csv', encoding='UTF-8')as f:
    csvStr = csv.reader(f)

    brithdate = []
    for x in csvStr:
        brithdate += [int(x[9])]
    ages = [99 - x for x in brithdate]
    average = sum(ages) / len(ages)
    print('2010村里長候選人平均年齡:', average)

    Number_of_differences = [x - average for x in ages]
    Number_of_differences_pow = [y ** 2 for y in Number_of_differences]
    Variation = sum(Number_of_differences_pow) / len(Number_of_differences_pow)
    Standard_deviation = Variation ** 0.5
    print('    標準差            :', Standard_deviation)

    # agess = 0
    # for y in range(len(ages)):
    #     agess += (ages[y] - (sum(ages) / len(ages))) ** 2
    # else:
    #     print((agess / len(ages)) ** 0.5)
    #     print(((Number_of_differences ** 2) / len(Number_of_differences)) ** 0.5)
