import cx_Oracle as oracle
import requests
import Ex99_api_key


# 경위도 변환 함수
def geocoding(store_info):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + store_info[1]
    rest_api_key = Ex99_api_key.rest_api_key
    headers = {"Authorization": 'KakaoAK ' + rest_api_key}
    try:
        req = requests.get(url, headers=headers)
    except Exception as e:
        print(store_info)
        print(e)
        store_infos.append(store_info)
        return 0
    else:
        if req.status_code == 200 and req.json()['documents']:
            result_address = req.json()['documents'][0]['address']
            # print(result_address['x'])
            # print(type(result_address['x']))
            x_y = {'x': result_address['x'], 'y': result_address['y']}
            return x_y
        else:
            return 0
    # print(req)
    # print(req.json())


# 데이터베이스에 입력
conn = oracle.connect('choe/1234@localhost:1521/xe')
cursor = conn.cursor()

update_sql = '''
UPDATE JADAM
SET LONGITUDE=:x, LATITUDE=:y
WHERE STORE_NAME = :name
'''

select_sql = '''
SELECT STORE_NAME, STORE_ADDR
FROM JADAM
'''

cursor.execute(select_sql)
store_infos = cursor.fetchall()
# print(store_infos)
# print(type(store_infos))

store_x_y_list = []
while store_infos:
    store_info = store_infos.pop()
    store_x_y = geocoding(store_info)
    if store_x_y:
        store_x_y_dict = {'name': store_info[0], 'x': store_x_y['x'], 'y': store_x_y['y']}
        store_x_y_list.append(store_x_y_dict)
# print(store_x_y_list)
# print(len(store_x_y_list))

for store_x_y in store_x_y_list:
    print(store_x_y)
    cursor.execute(update_sql, store_x_y)

conn.commit()
cursor.close()
conn.close()
