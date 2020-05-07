emp = {}
emp['id'] = 1
emp['name'] = 'mary'
addr1 = {'county': 'Kao', 'no': '100'}
addr2 = {'county': 'Tnn', 'no': '200'}
addr = [addr1, addr2]
emp['addr'] = addr
import json

jsonRep = json.dumps(emp)
print(jsonRep)
