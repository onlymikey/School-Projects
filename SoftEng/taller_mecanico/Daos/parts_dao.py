import mysql.connector
from database import get_connection
from Models.parts_model import Parts
class PartsDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbtaller_mecanico"
        )
        self.cursor = self.connection.cursor()

    def create_parts(self, parts: Parts):
        """Crea una nueva parte en la base de datos."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO piezas (descripcion, stock)
        VALUES (%s, %s)
        """
        values = (parts.description, parts.stock)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def get_parts_by_id(self, partid: int) -> Parts:
        """Obtiene una parte por su id."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM piezas WHERE id_pieza = %s"
        cursor.execute(query, (partid,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Parts(row['id_pieza'], row['descripcion'], row['stock'])
        return None

    def get_parts_by_name(self, name: str) -> Parts:
        """Obtiene una parte por su nombre."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM piezas WHERE descripcion = %s"
        cursor.execute(query, (name,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Parts(row['id_pieza'], row['descripcion'], row['stock'])
        return None

    def update_parts(self, parts: Parts):
        """Actualiza la información de una parte."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE piezas
        SET descripcion = %s, stock = %s
        WHERE id_pieza = %s
        """
        values = (parts.description, parts.stock, parts.partid)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def get_all_parts_names(self):
        """Obtiene todos los nombres de las partes."""
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT descripcion FROM piezas"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [row[0] for row in rows]