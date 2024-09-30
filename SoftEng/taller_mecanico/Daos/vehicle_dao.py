import mysql.connector
from database import get_connection
from Models.vehicle_model import Vehicle
class UserDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbtaller_mecanico"
        )
        self.cursor = self.connection.cursor()

    def create_vehicle(self, vehicle: Vehicle):
        """Crea un nuevo usuario en la base de datos."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO usuarios (matricula, marca, modelo)
        VALUES (%s, %s, %s)
        """
        values = (vehicle.registration, vehicle.brand, vehicle.model)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def read_vehicle_by_registration(self, registration: str) -> Vehicle:
        """Obtiene un vehiculo por su matricula."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM vehiculos WHERE matricula = %s"
        cursor.execute(query, (registration,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Vehicle(row['matricula'], row['marca'], row['clientid'], row['modelo'])
        return None

    def update_vehicle(self, vehicle: Vehicle):
        """Actualiza la información de un vehículo existente en la base de datos."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE vehiculos
        SET marca = %s, modelo = %s
        WHERE matricula = %s
        """
        values = (vehicle.brand, vehicle.model, vehicle.registration)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
