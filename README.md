# Mapping.Python

## Descripción del Proyecto

Este proyecto utiliza la biblioteca `folium` para crear mapas interactivos en Python. El objetivo principal es proporcionar una guía práctica para generar mapas personalizados, agregar marcadores y guardar los resultados en archivos HTML que pueden visualizarse en cualquier navegador web.

El proyecto incluye un ejemplo funcional que centra un mapa en Bogotá, Colombia, con un marcador interactivo. Este ejemplo puede ser modificado fácilmente para adaptarse a otras ubicaciones y configuraciones.

---

## Contenido del Proyecto

El proyecto contiene los siguientes archivos y directorios:

- **`Instruction.md`**: Una guía detallada para instalar y usar `folium` para crear mapas interactivos.
- **`map1.py`**: Un script de Python que genera un mapa interactivo centrado en Bogotá, Colombia, con un marcador.
- **`Map1.html`**: Un archivo HTML generado por el script `map1.py`, que contiene el mapa interactivo.
- **`path/to/venv/`**: Un entorno virtual de Python configurado para este proyecto.
- **`README.md`**: Este archivo, que describe el proyecto y proporciona instrucciones para configurarlo y ejecutarlo.

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

1. **Python 3.13 o superior**: Puedes verificar tu versión de Python ejecutando `python3 --version` en tu terminal.
2. **pip**: El gestor de paquetes de Python. Generalmente viene preinstalado con Python.
3. **Entorno virtual (opcional)**: Se recomienda usar un entorno virtual para evitar conflictos de dependencias.

---

## Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local:

### 1. Clonar el Repositorio
Clona este repositorio en tu máquina local utilizando el siguiente comando:

```bash
git clone https://github.com/SoyEdwinCabrera/Mapping.Python
cd mapping
```

### 2. Crear un Entorno Virtual (opcional)

```bash
python3 -m venv path/to/venv
source path/to/venv/bin/activate  # En macOS/Linux
path\to\venv\Scripts\activate     # En Windows
```

### 3. Instalar Dependencias

```bash
pip install folium
```

Uso del Proyecto

### 1. Ejecutar el Script
Ejecuta el script `map1.py` para generar un mapa interactivo:

```bash
python3 mapping/map1.py
```

Esto generará un archivo HTML llamado `map1.html` en el directorio raíz del proyecto.

### 2. Visualizar el Mapa
Abre el archivo `map1.html` en tu navegador web para visualizar el mapa interactivo.

---

## Personalización

Puedes personalizar el mapa modificando el archivo `map1.py`. Algunas opciones incluyen:

1. **Cambiar la ubicación del mapa**:
   Modifica el parámetro `location` en la línea donde se crea el mapa:

   ```python
   map = folium.Map(location=[LATITUD, LONGITUD], zoom_start=6)
   ```

2. **Agregar más marcadores**:
   Usa el método `add_child` para agregar más marcadores al grupo de características:

   ```python
   fg.add_child(folium.Marker(
       location=[LATITUD, LONGITUD],
       popup="Descripción del marcador",
       icon=folium.Icon(color="blue")
   ))
   ```

3. **Cambiar el estilo del mapa**:
   Modifica el parámetro `tiles` para usar diferentes estilos de mapa, como `Stamen Terrain` o `OpenStreetMap`.

---

## Estructura del Proyecto

```plaintext
mapping/
├── Instruction.md       # Guía de instalación y uso de folium
├── Map1.html            # Mapa interactivo generado
├── README.md            # Este archivo
├── map1.py              # Script de Python para generar el mapa
└── path/
    └── to/
        └── venv/        # Entorno virtual de Python
```

---

## Recursos Adicionales

- [Documentación oficial de Folium](https://python-visualization.github.io/folium/)
- [Documentación de Python](https://docs.python.org/3/)

---

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request en este repositorio.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles