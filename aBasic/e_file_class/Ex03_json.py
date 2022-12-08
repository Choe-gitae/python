# Ex03_json.py

file = open('data/temp.json', 'r', encoding='utf-8-sig')
data = file.read()
file.close()

print(data)
print(type(data))


import json
json_data = json.loads(data)

print(json_data)
print(type(json_data))

for k, v in json_data.items():
    print(k, '>', v)
    print(k, '>>', v['Job'])
