import mysql.connector
from database import get_connection
from Models.repair_model import Repair
class RepairDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbtaller_mecanico"
        )
        self.cursor = self.connection.cursor()

    def create_repair(self, repair: Repair):
        """Crea una nueva reparación en la base de datos."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO reparaciones (matricula, id_pieza, fecha_entrada, fecha_salida, cantidad, problema)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (repair.matricula, repair.id_part, repair.in_date, repair.out_date, repair.quantity, repair.problem)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def get_repair_by_id(self, id_repair: int) -> Repair:
        """Obtiene una reparación por su id."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM reparaciones WHERE id_reparacion = %s"
        cursor.execute(query, (id_repair,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Repair(row['id_reparacion'], row['matricula'], row['id_pieza'], row['fecha_entrada'], row['fecha_salida'], row['cantidad'], row['problema'])
        return None

    def update_repair(self, repair: Repair):
        """Actualiza la información de una reparación."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE reparaciones
        SET matricula = %s, id_pieza = %s, fecha_entrada = %s, fecha_salida = %s, cantidad = %s, problema = %s
        WHERE id_reparacion = %s
        """
        values = (repair.matricula, repair.id_part, repair.in_date, repair.out_date, repair.quantity, repair.problem, repair.id_repair)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()