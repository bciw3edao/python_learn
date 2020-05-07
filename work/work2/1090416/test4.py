emp = {}
emp['id'] = 1
emp['name'] = 'mary'
print(emp, type(emp))

import json

jsonRep = json.dumps(emp)
print(jsonRep, type(jsonRep))
