# Adding HTML on Popups

Si deseas tener texto estilizado (negritas, diferentes fuentes, etc.) en la ventana emergente (popup), puedes usar HTML. A continuación, se muestra un ejemplo:

## Ejemplo básico: Texto estilizado en el popup

```python
import folium
import pandas

# Cargar datos desde un archivo CSV
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])  # Lista de latitudes
lon = list(data["LON"])  # Lista de longitudes
elev = list(data["ELEV"])  # Lista de elevaciones

# Plantilla HTML para el popup
html = """<h4>Volcano information:</h4>
Height: %s m
"""

# Crear un mapa base
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

# Agregar marcadores con popups
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

# Agregar el grupo de características al mapa
map.add_child(fg)

# Guardar el mapa en un archivo HTML
map.save("Map_html_popup_simple.html")
```

## Ejemplo avanzado: Enlaces en el popup

También puedes incluir enlaces en la ventana emergente. Por ejemplo, el siguiente código genera una ventana emergente con el nombre del volcán como un enlace que realiza una búsqueda en Google para ese volcán cuando se hace clic.

```python
import folium
import pandas

# Cargar datos desde un archivo CSV
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])  # Lista de latitudes
lon = list(data["LON"])  # Lista de longitudes
elev = list(data["ELEV"])  # Lista de elevaciones
name = list(data["NAME"])  # Lista de nombres de volcanes

# Plantilla HTML para el popup con un enlace
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# Crear un mapa base
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

# Agregar marcadores con popups
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

# Agregar el grupo de características al mapa
map.add_child(fg)

# Guardar el mapa en un archivo HTML
map.save("Map_html_popup_advanced.html")
```

## Explicación de los elementos clave

1. **HTML en el popup**:
   - Puedes usar etiquetas HTML como `<h4>`, `<br>`, `<a>` para estilizar el contenido del popup.
   - En el ejemplo avanzado, el enlace utiliza la etiqueta `<a>` con un atributo `href` que apunta a una búsqueda en Google.

2. **Uso de `folium.IFrame`**:
   - Permite incrustar contenido HTML en el popup.
   - Los parámetros `width` y `height` controlan el tamaño del popup.

3. **Personalización del ícono**:
   - El color del ícono se define con `folium.Icon(color="green")`.

4. **Guardado del mapa**:
   - El mapa se guarda como un archivo HTML (`map.save("nombre_del_archivo.html")`), que puede abrirse en cualquier navegador.

## Resultado esperado

- **Ejemplo básico**: Un popup con texto estilizado que muestra la altura del volcán.
- **Ejemplo avanzado**: Un popup con el nombre del volcán como un enlace que realiza una búsqueda en Google.

¡Con estos ejemplos, puedes crear mapas interactivos con ventanas emergentes personalizadas y estilizadas!