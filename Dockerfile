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

# Variable de entorno de mongo
ENV MONGO_URI=mongodb+srv://alejandroramirez3:Ar1193099884@distribuidos.monke8z.mongodb.net/?retryWrites=true&w=majority&appName=distribuidos

# Comando para correr la aplicacion
CMD ["python", "app.py"]
