# Ex02_csv.py
import csv

# csv 파일 -> 엑셀에서 열림 + 일반 에디터에서 열림
# Common String Value

data = [
    [1, '김', '책임'],
    [2, '박', '선임'],
    [3, '맹', '연구원'],
]
# with open('data/imsi.csv', 'x', encoding='utf-8-sig') as file:
#     # file.write(data)
#     csvout = csv.writer(file)
#     csvout.writerows(data)

result = []
with open('data/imsi.csv', 'r', encoding='utf-8-sig') as file:
    csvin = csv.reader(file)
    result = [row for row in csvin if row]

print(result)
