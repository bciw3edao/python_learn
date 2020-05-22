import csv

with open(r'..\voteData\2010村里長\elcand.csv', encoding='UTF-8')as f:
    csvStr = csv.reader(f)

    brithdate = []
    for x in csvStr:
        brithdate += [int(x[9])]
    ages = [99-x for x in brithdate]
    print('2010村里長候選人平均年齡:',sum(ages)/len(ages))
    
    # SumAge = 0
    # Number_of_people = 0
    # for y in csvStr:
    #     SumAge += (99 - int(y[9]))
    #     Number_of_people += 1
    # else:
    #     print('2010村里長候選人平均年齡:', SumAge / Number_of_people)
