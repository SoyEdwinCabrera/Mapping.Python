# **Guía de Referencia: Instalación y Uso Básico de `folium` para Crear Mapas Interactivos**

Esta guía proporciona instrucciones claras y concisas para instalar la biblioteca `folium`, explorar sus funcionalidades y crear mapas interactivos en Python. Sigue los pasos a continuación para comenzar.

---

## **1. Instalación de `folium`**
Para instalar la biblioteca `folium`, utiliza el siguiente comando en tu terminal o línea de comandos:

```bash
pip3 install folium
```

### **Detalles del proceso de instalación:**
- `pip3` descargará e instalará `folium` y sus dependencias necesarias, como `branca`.
- Si algunas dependencias ya están instaladas (por ejemplo, `jinja2`, `numpy`, `requests`), `pip3` las detectará y no las descargará nuevamente.
- Una vez completada la instalación, deberías ver un mensaje como:
  ```plaintext
  Successfully installed branca-0.8.1 folium-0.19.5
  ```

---

## **2. Iniciar el intérprete de Python**
Abre el intérprete interactivo de Python 3 para probar la biblioteca recién instalada. Ejecuta el siguiente comando en tu terminal:

```bash
python3
```

Deberías ver algo similar a:
```plaintext
Python 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 08:22:19) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

---

## **3. Importar la biblioteca `folium`**
Dentro del intérprete de Python, importa la biblioteca `folium` con el siguiente comando:

```python
import folium
```

Si la importación es exitosa, no se mostrará ningún mensaje de error.

---

## **4. Explorar las funcionalidades de `folium`**
Para ver una lista de las clases, métodos y atributos disponibles en `folium`, utiliza el comando `dir()`:

```python
dir(folium)
```

Esto mostrará una lista de elementos como:
```plaintext
['Choropleth', 'Circle', 'CircleMarker', 'Map', 'Marker', 'Popup', 'TileLayer', ...]
```

---

## **5. Crear un mapa básico**
Crea un mapa interactivo utilizando la clase `folium.Map`. Por ejemplo:

```python
map = folium.Map(location=[90, -180])
```

### **Detalles:**
- El parámetro `location` define las coordenadas iniciales del mapa en formato `[latitud, longitud]`.
- `[90, -180]` corresponde a un punto en el extremo noreste del globo terráqueo.
- Utiliza herramientas como GoogleMaps para obtener las coordenadas de un lugar específico.

---

## **6. Guardar el mapa en un archivo HTML**
Para visualizar el mapa, guárdalo en un archivo HTML que pueda abrirse en un navegador web:

```python
map.save("Map1.html")
```

### **Resultado:**
- Se generará un archivo llamado `Map1.html` en el directorio actual.
- Ábrelo en tu navegador para ver el mapa interactivo.

---

## **7. Crear un mapa con coordenadas específicas**
Puedes centrar el mapa en una ubicación específica proporcionando las coordenadas de latitud y longitud. Por ejemplo, para centrar el mapa en Bogotá, Colombia:

```python
map = folium.Map(location=[4.60315184339365, -74.0723895515354])
map.save("Map1.html")
```

### **Detalles:**
- `[4.60315184339365, -74.0723895515354]` son las coordenadas de Bogotá.
- El archivo `Map1.html` se sobrescribirá con el nuevo mapa.

---

## **8. Ajustar el nivel de zoom**
Puedes personalizar el nivel de detalle inicial del mapa utilizando el parámetro `zoom_start`. Por ejemplo:

```python
map = folium.Map(location=[4.60315184339365, -74.0723895515354], zoom_start=6)
map.save("Map1.html")
```

### **Detalles:**
- `zoom_start=6` establece el nivel de zoom inicial. Valores más altos acercan el mapa, mientras que valores más bajos lo alejan.
- Guarda el mapa nuevamente en `Map1.html` para visualizar los cambios.

---

## **Resumen de Comandos**
| **Acción**                          | **Comando**                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
| Instalar `folium`                   | `pip3 install folium`                                                      |
| Iniciar el intérprete de Python     | `python3`                                                                  |
| Importar `folium`                   | `import folium`                                                            |
| Crear un mapa básico                | `map = folium.Map(location=[90, -180])`                                    |
| Guardar el mapa en un archivo HTML  | `map.save("Map1.html")`                                                    |
| Crear un mapa con coordenadas       | `map = folium.Map(location=[latitud, longitud])`                           |
| Ajustar el nivel de zoom            | `map = folium.Map(location=[latitud, longitud], zoom_start=nivel_de_zoom)` |

---

## **Notas Finales**
- El archivo HTML generado puede abrirse en cualquier navegador para visualizar el mapa interactivo.
- `folium` es una herramienta poderosa para crear mapas personalizados y visualizaciones geográficas. Explora más funcionalidades consultando la documentación oficial: [Folium Documentation](https://python-visualization.github.io/folium/).


**********************************************************************************************************************************************************