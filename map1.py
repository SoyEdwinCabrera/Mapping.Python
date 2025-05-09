import folium  # Importa la biblioteca folium para crear mapas interactivos
import pandas

data = pandas.read_csv("bares_rock_bogota.txt")  # Lee un archivo CSV llamado "data.csv" y lo almacena en un DataFrame
lat =list(data["LAT"])  # Extrae la columna "latitud" del DataFrame y la convierte en una lista
lon =list(data["LON"])  # Extrae la columna "longitud" del DataFrame y la convierte en una lista
name = list(data["NAME"])  
genre = list(data["TYPE"]) 
status = list(data["STATUS"])

def color_producer(status):
    if status == "Abierto":
        return 'blue'
    elif status == "Cerrado":
        return 'red'
    
# Crea un mapa base centrado en Bogotá, Colombia, con un nivel de zoom inicial de 6
map = folium.Map(
    location=[4.6031, -74.072],  # Coordenadas del centro del mapa (latitud, longitud)
    zoom_start=12,                # Nivel de zoom inicial
    tiles="OpenStreetMap"      # Estilo del mapa (CartoDB Voyager)
)

# Crea un grupo de características para agregar elementos al mapa
fgv = folium.FeatureGroup(name="Bares de Rock en Bogotá")

# Agrega un marcador al grupo de características
for lt, ln, nm, gn, sts in zip(lat, lon, name, genre, status):
    fgv.add_child(folium.Marker(
        location=[lt, ln],  # Coordenadas del marcador (latitud, longitud)
        popup=nm +" "+ gn ,    # Mensaje emergente que aparece al hacer clic en el marcador
        icon=folium.Icon(color=color_producer(sts)),  # Ícono del marcador con color verde
    ))
    
# Abrir y leer el archivo GeoJSON
with open('world.json', 'r', encoding='utf-8-sig') as file:
    geojson_data = file.read()

fgp = folium.FeatureGroup(name="Population")

# Agregar los datos GeoJSON al grupo de características con estilo
fgp.add_child(folium.GeoJson(
    data=geojson_data,  # Pasar los datos GeoJSON como cadena
    style_function=lambda x: {'fillColor': 'green' if x['properties']["POP2005"] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}  #else Estilo para las geometrías
))

# ESte codigo es para cambiar el tipo de marca a un círculo en el mapa
# for coordinates in [[4.6031, -74.072], [4.7031, -75.072]]:
#     fgv.add_child(folium.CircleMarker(
#         location=coordinates,  # Coordenadas del marcador (latitud, longitud)
#         radius=10,             # Radio del círculo en píxeles
#         popup="Hi, I am a Point",  # Mensaje emergente que aparece al hacer clic en el punto
#         color="blue",          # Color del borde del círculo
#         fill=True,             # Rellenar el círculo
#         fill_color="blue",     # Color de relleno del círculo
#         fill_opacity=0.6       # Opacidad del relleno (0.0 a 1.0)
#     ))


# Agrega el grupo de características al mapa principal
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())  # Agrega un control de capas al mapa

# Guarda el mapa generado en un archivo HTML llamado "Map1.html"
map.save("Map1.html")
