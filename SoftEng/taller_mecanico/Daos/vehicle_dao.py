import mysql.connector
from database import get_connection
from Models.vehicle_model import Vehicle
class VehicleDAO:
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
        INSERT INTO vehiculos (matricula, cliente_id, marca, modelo)
        VALUES (%s, %s, %s, %s)
        """
        values = (vehicle.registration, vehicle.clientid, vehicle.brand, vehicle.model)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def get_vehicle_by_registration(self, registration: str) -> Vehicle:
        """Obtiene un vehiculo por su matricula."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM vehiculos WHERE matricula = %s"
        cursor.execute(query, (registration,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Vehicle(row['matricula'], row['cliente_id'], row['marca'], row['modelo'])
        return None

    def update_vehicle(self, vehicle: Vehicle):
        """Actualiza la información de un vehículo existente en la base de datos."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE vehiculos
        SET marca = %s, modelo = %s, cliente_id = %s
        WHERE matricula = %s
        """
        values = (vehicle.brand, vehicle.model, vehicle.clientid, vehicle.registration)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
