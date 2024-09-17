from bs4 import BeautifulSoup
import requests
import pandas as pd
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def scrape_and_save():
    # Mostrar un cuadro de diálogo para ingresar la URL
    url = simpledialog.askstring("Ingresar URL", "Por favor, ingresa la URL de la página:")
    
    if not url:
        messagebox.showerror("Error", "No se ingresó ninguna URL.")
        return

    try:

        # Obtener el contenido de la página
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html')

        # Encontrar todas las tablas en la página
        tables = soup.find_all('table')
        
        if not tables:
            messagebox.showerror("Error", "No se encontraron tablas en la página.")
            return
        
        # Mostrar un cuadro de diálogo para que el usuario ingrese el número de la tabla
        table_index = simpledialog.askinteger(
            "Elegir Tabla", 
            f"Se encontraron {len(tables)} tablas. Elija el n° de la tabla a obtener (0 equivale a la primera tabla):",
            minvalue=0, maxvalue=len(tables)-1
        )

        if table_index is None:
            messagebox.showerror("Error", "No se seleccionó ninguna tabla.")
            return


        # Encontrar la primera tabla en la página
        table = tables[table_index]
        table_titles = table.find_all('th')
        table_titles_extraction = [title.text.strip() for title in table_titles]


        # Crear un DataFrame con los títulos de las columnas
        dataf = pd.DataFrame(columns = table_titles_extraction)

        # Extraer los datos de cada fila de la tabla
        column_data = table.find_all('tr')
        for row in column_data[1:]:
            row_data = row.find_all('td')
            individual_row_data = [data.text.strip() for data in row_data]
            length = len(dataf)
            dataf.loc[length] = individual_row_data

        # Mostrar el cuadro de diálogo "Guardar como"
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",  # Extensión predeterminada del archivo
            filetypes=[("Archivo de valores separados por comas", "*.csv"), ("All files", "*.*")],  # Tipos de archivo permitidos
            title="Guardar como"  # Título de la ventana
            )
    
    
        # Guardar el archivo CSV
        if file_path:
            dataf.to_csv(file_path, index=False)
            messagebox.showinfo("Éxito", f"Archivo guardado en: {file_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Web Scraper")

# Añadir un botón para iniciar el proceso de scraping
scrape_button = tk.Button(root, text="Iniciar Web Scraping", command=scrape_and_save)
scrape_button.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()