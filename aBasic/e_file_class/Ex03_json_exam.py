# Ex03_json_exam.py

'''
data / sample.json 파일을 읽고 총합 구해서 출력
'''

import json
with open('data/sample.json', 'r', encoding='utf-8-sig') as file:
    file_context = file.read()
    json_data = json.loads(file_context)
    total = 0
    for value in json_data.values():
        if value:
            total += value['price'] * value['count']
    print(total)
