import folium
import pandas

Volcanoes = pandas.read_csv('Volcanoes.txt')
lat = list(Volcanoes["LAT"])
lon = list(Volcanoes["LON"])
name = list(Volcanoes["NAME"])
elev = list(Volcanoes["ELEV"])
map = folium.Map(location=[34.2070,-77.95])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000< elevation < 3000:
        return 'orange'
    else:
        return 'red'

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, name, el in zip(lat, lon, name, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 10,
                 popup=str(el)+" m "+name, fill_color=color_producer(el),
                 fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                          else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
                          else 'red'}))


map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())


map.save("Map1.html")
