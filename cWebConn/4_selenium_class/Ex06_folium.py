import folium

# zoom_start 보통 16~19  # tiles 지도 모양 검색해서 맘에 드는 걸로
map_osm = folium.Map(location=[37.572807, 126.975912], zoom_start=17)
folium.Marker(location=[37.572807, 126.975912],
              popup='세종문화회관',
              icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)
map_osm.save('./map/map5.html')

# map_osm = folium.Map(location=[36.5, 128], zoom_start=8)
# map_osm.save('./map/map_test.html')
