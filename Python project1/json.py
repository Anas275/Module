import json
d='{"name":"python","fees":12000,"duration":"2 months"}'
x=json.loads(d)
print(type(x))
print(x)