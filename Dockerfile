# Usa una imagen base de Python
FROM python:3.9-slim

# Instala dependencias del sistema para tkinter
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Crea un directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script al contenedor
COPY Webscrapping\ Python.py .

# Define el comando predeterminado para ejecutar el script
CMD ["python", "Webscrapping Python.py"]