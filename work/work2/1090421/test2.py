jasonStr = '{"id": 1, "name": "mary", "addr": ["Kao", "Tnn"]}'
import json

dic = json.loads(jasonStr)
print(dic['id'])
addr = dic['addr']
for x in addr:
    print(x)
