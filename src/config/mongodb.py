from pymongo import MongoClient
import certifi
# from dotenv import load_dotenv
import os

# Cargar variables de entorno
# load_dotenv()

# URI de conexión a MongoDB
MONGO_URI = os.getenv("MONGO_URI")
# Certificado de conexión
ca = certifi.where()

# Función para conectar a la base de datos
def dbConnection():
    # Conexión a la base de datos
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client['db_tasks']
    # Manejo de error de conexión
    except ConnectionError:
        print("Error de conexión")

    # Retornar la conexión
    return db

