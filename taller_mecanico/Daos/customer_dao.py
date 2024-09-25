import mysql.connector
from database import get_connection
from Models.customer_model import Customer
class CustomerDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbtaller_mecanico"
        )
        self.cursor = self.connection.cursor()

    def save_customer(self, customer: Customer):
        """Crea un nuevo usuario en la base de datos."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO clientes (nombre, telefono)
        VALUES (%s, %s, %s)
        """
        values = (customer.name, customer.phone)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def get_customer_by_id(self, customer_id: int) -> Customer:
        """Obtiene un usuario por su ID."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM clientes WHERE cliente_id = %s"
        cursor.execute(query, (customer_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Customer(row['cliente_id'], row['nombre'], row['telefono'])
        return None

    def update_customer(self, customer: Customer):
        """Actualiza la información de un usuario existente en la base de datos."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE clientes
        SET nombre = %s, telefono = %s
        """
        values = (customer.name, customer.phone)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()