from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

table = soup.find_all('table')[0]

table_titles = table.find_all('th')

table_titles_extraction = [title.text.strip() for title in table_titles]

print(table_titles_extraction)

dataf = pd.DataFrame(columns = table_titles_extraction)

print(dataf)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)

    length = len(dataf)
    dataf.loc[length] = individual_row_data

# Crear una instancia de la aplicación principal de Tkinter
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Mostrar el cuadro de diálogo "Guardar como"
file_path = filedialog.asksaveasfilename(
    defaultextension=".csv",  # Extensión predeterminada del archivo
    filetypes=[("Archivo de valores separados por comas", "*.csv"), ("All files", "*.*")],  # Tipos de archivo permitidos
    title="Guardar como"  # Título de la ventana
)

# Comprueba si el usuario seleccionó un archivo
if file_path:
    # Guarda el contenido en la ruta especificada
    dataf.to_csv(file_path, index=False)  # Usa index=True si quieres incluir el índice en el archivo CSV

print(f"Archivo guardado en: {file_path}")