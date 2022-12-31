import folium
import cx_Oracle as oracle
import Ex99_api_key

vworld_key = Ex99_api_key.vworld_key
layer = "Base"
tileType = "png"
tiles = f"http://api.vworld.kr/req/wmts/1.0.0/{vworld_key}/{layer}/{{z}}/{{y}}/{{x}}.{tileType}"
attr = "Vworld"

map = folium.Map(location=[36, 128], zoom_start=7)

folium.TileLayer(
    tiles=tiles,
    attr=attr,
    overlay=True,
    control=True
).add_to(map)

conn = oracle.connect('choe/1234@localhost:1521/xe')
cursor = conn.cursor()

select_sql = '''
SELECT STORE_NAME, LATITUDE, LONGITUDE
FROM JADAM
'''

cursor.execute(select_sql)
data = cursor.fetchall()
# print(data)
# print(type(data))

for store in data:
    print(store)
    if store[0] and store[1] and store[2]:
        folium.Marker(location=[store[1], store[2]],
                      popup=store[0],
                      icon=folium.Icon(color='purple', icon='info-sign')).add_to(map)

map.save('./jadam/map.html')
