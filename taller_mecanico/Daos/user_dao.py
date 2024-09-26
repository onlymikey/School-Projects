import mysql.connector
from database import get_connection
from Models.user_model import User
class UserDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbtaller_mecanico"
        )
        self.cursor = self.connection.cursor()
    
    def create_user(self, user: User):
        """Crea un nuevo usuario en la base de datos."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO usuarios (nombre, username, password, perfil)
        VALUES (%s, %s, %s, %s)
        """
        values = (user.name, user.username, user.password, user.profile)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def read_user_by_username(self, username: str) -> User:
        """Obtiene un usuario por su nombre de usuario."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE username = %s"
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return User(row['usuario_id'], row['nombre'], row['username'], row['password'], row['perfil'])
        return None

    def get_user_by_id(self, user_id: int) -> User:
        """Obtiene un usuario por su ID."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE usuario_id = %s"
        cursor.execute(query, (user_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return User(row['usuario_id'], row['nombre'], row['username'], row['password'], row['perfil'])
        return None

    def update_user(self, user: User):
        """Actualiza la información de un usuario existente en la base de datos."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE usuarios
        SET nombre = %s, username = %s, password = %s, perfil = %s
        WHERE usuario_id = %s
        """
        values = (user.name, user.username, user.password, user.profile, user.id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def delete_user(username: str):
        """Elimina un usuario por su nombre de usuario."""
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM usuarios WHERE username = %s"
        cursor.execute(query, (username,))
        conn.commit()
        cursor.close()
        conn.close()

    def list_all_users():
        """Devuelve una lista de todos los usuarios."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuarios"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [User(row['nombre'], row['username'], row['password'], row['perfil']) for row in rows]
    
    def verify_user(self, username, password):
        """Verificar si las credenciales coinciden con algún registro en la base de datos."""
        query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
        self.cursor.execute(query, (username, password))
        result = self.cursor.fetchone()  # Devuelve una tupla si coincide o None si no hay coincidencia
        return result is not None

