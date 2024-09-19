import mysql.connector
from mysql.connector import Error

def create_connection():
    """ Crea y retorna la conexión a la base de datos. """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dbtaller_mecanico'
        )
        if connection.is_connected():
            print("Conexión a la base de datos establecida.")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def get_connection():
    """Establece y devuelve una conexión a la base de datos."""
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Actualiza según tu configuración
        database='dbtaller_mecanico'
    )
    return connection

def close_connection(connection):
    """ Cierra la conexión a la base de datos. """
    if connection.is_connected():
        connection.close()
        print("Conexión a la base de datos cerrada.")
