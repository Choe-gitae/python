from geopy.geocoders import Nominatim
import cx_Oracle as oracle

geo_local = Nominatim(user_agent='South Korea')


# 위도, 경도 반환하는 함수
def geocoding(address):
    try:
        geo = geo_local.geocode(address)
        x_y = {'longitude': geo.longitude, 'latitude': geo.latitude}
        return x_y
    except:
        return 0


conn = oracle.connect('choe/1234@localhost:1521/xe')
cursor = conn.cursor()

update_sql = '''
UPDATE JADAM
SET LONGITUDE=:longitude, LATITUDE=:latitude
WHERE STORE_NAME = :name
'''

select_sql = '''
SELECT STORE_NAME, STORE_ADDR
FROM JADAM
'''

cursor.execute(select_sql)
store_info = cursor.fetchall()
# print(store_info)
# print(type(store_info))

geo_list = []
for info in store_info:
    store_geo = geocoding(info[1])
    print(store_geo)
    if store_geo:
        store_geo_dict = {'name': info[0], 'longitude': store_geo['longitude'], 'latitude': store_geo['latitude']}
        geo_list.append(store_geo_dict)
# print(geo_list)

for geo in geo_list:
    # print(geo)
    cursor.execute(update_sql, geo)

conn.commit()
cursor.close()
conn.close()
