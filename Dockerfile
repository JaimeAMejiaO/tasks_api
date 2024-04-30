FROM python:3.12

# Seteando el directorio de trabajo
WORKDIR /app

# Instalando requerimientos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiando la aplicacion dentro de carpeta "app"
COPY /src/ .

# Exponiendo el puerto 5000
EXPOSE 5000

# La variable de entorno de mongo_uri la defino en el mismo servidor para evitar que se vea en el repositorio

# Comando para correr la aplicacion
CMD ["python", "app.py"]
