# Webscrapping de Tablas con Python
Este script de Python realiza web scraping en la página que especifique, extrae los datos en una tabla y los guarda en un archivo CSV en la ubicación especificada por el usuario.

## Requisitos

- Python 3.x
- Paquetes de Python:
  - `beautifulsoup4`
  - `requests`
  - `pandas`
  - `tkinter` (incluido con Python)

Puedes instalar los paquetes necesarios con el siguiente comando:
***
pip install beautifulsoup4 requests pandas
***

## Descripción del Script
1. Interfaz Gráfica: El script utiliza tkinter para crear una interfaz gráfica que permite al usuario:
* Ingresar la URL de la página web que contiene la tabla.
* Seleccionar el número de la tabla a extraer si la página contiene más de una.
* Elegir la ubicación y el nombre del archivo para guardar los datos extraídos en formato CSV.

2. Extracción de Datos:

* Utiliza requests para obtener el contenido de la página web y BeautifulSoup para analizar el contenido HTML.
* Encuentra todas las tablas en la página y permite al usuario seleccionar cuál desea extraer.
* Extrae los datos de la tabla seleccionada y los guarda en un DataFrame de pandas.

3. Guardar los Datos: Utiliza la librería tkinter para abrir un cuadro de diálogo "Guardar como", permitiendo al usuario seleccionar la ubicación y el nombre del archivo CSV en el que se guardarán los datos extraídos.

## Cómo Usar el Script
1. Ejecuta el script. Puedes hacerlo desde una terminal con el siguiente comando:
***
python nombre_del_script.py
***

2. La interfaz gráfica mostrará un botón "Iniciar Web Scraping".

3. Al hacer clic en el botón, se abrirá un cuadro de diálogo donde podrás ingresar la URL de la página web.

4. Luego, se abrirá otro cuadro de diálogo solicitando el número de la tabla a extraer (0 equivale a la primera tabla).

5. Después de seleccionar la tabla, se mostrará un cuadro de diálogo "Guardar como" para elegir la ubicación y el nombre del archivo CSV.

6. El archivo CSV se guardará en la ubicación especificada, y el script mostrará un mensaje de confirmación.

## Notas
* El script permite al usuario seleccionar una tabla específica en la página web, incluso si hay múltiples tablas disponibles.
* Asegúrate de que la estructura de la página web no cambie, ya que podría afectar la extracción de datos.
* El cuadro de diálogo "Guardar como" permite seleccionar la ubicación y el nombre del archivo. El archivo se guarda en formato CSV.

## Créditos
Este script utiliza las siguientes bibliotecas de Python:

* requests para realizar solicitudes HTTP.
* BeautifulSoup para analizar el contenido HTML.
* pandas para manipular y guardar los datos en un archivo CSV.
* tkinter para mostrar el cuadro de diálogo "Guardar como".
* El canal de YouTube @Alex The Analyst, quien hizo este producto y sólo se le introdujeron algunos cambios. 