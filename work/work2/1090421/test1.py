emp = {}
emp['id'] = 1
emp['name'] = 'mary'
addr = ['Kao', 'Tnn']
emp['addr'] = addr
import json

jsonRep = json.dumps(emp)
print(jsonRep, type(jsonRep))
