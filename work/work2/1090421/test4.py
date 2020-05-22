jsonStr ='{"id": 1, "name": "mary", "addr": [{"county": "Kao", "no": "100"}, {"county": "Tnn", "no": "200"}]}'
import json
dic=json.loads(jsonStr)
print(dic['id'])
addrDic = dic['addr']
for x in addrDic:
    print(x['county'])