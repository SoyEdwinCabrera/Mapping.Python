
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
fg = folium.FeatureGroup(name="My Map")

# Agrega un marcador al grupo de características
for lt, ln, nm, gn, sts in zip(lat, lon, name, genre, status):
    fg.add_child(folium.Marker(
        location=[lt, ln],  # Coordenadas del marcador (latitud, longitud)
        popup=nm +" "+ gn ,    # Mensaje emergente que aparece al hacer clic en el marcador
        icon=folium.Icon(color=color_producer(sts))  # Ícono del marcador con color verde
    ))

# Agrega el grupo de características al mapa principal
map.add_child(fg)

# Guarda el mapa generado en un archivo HTML llamado "Map1.html"
map.save("Map1.html")
