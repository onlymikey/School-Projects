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
        INSERT INTO clientes (nombre, telefono, usuario_id)
        VALUES (%s, %s, %s)
        """
        values = (customer.name, customer.phone, customer.userid)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def get_customer_by_id(self, customer_id: int) -> Customer:
        """Obtiene un Cliente por su ID."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM clientes WHERE cliente_id = %s"
        cursor.execute(query, (customer_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Customer(row['cliente_id'], row['nombre'], row['telefono'], row['usuario_id'])
        return None

    def get_customer_by_name(self, name: str) -> Customer:
        """Obtiene un Cliente por su nombre."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM clientes WHERE nombre = %s"
        cursor.execute(query, (name,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Customer(row['cliente_id'], row['nombre'], row['telefono'], row['usuario_id'])
        return None

    def update_customer(self, customer: Customer):
        """Actualiza la información de un usuario existente en la base de datos."""
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE clientes
        SET nombre = %s, telefono = %s
        WHERE cliente_id = %s
        """
        values = (customer.name, customer.phone, customer.id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def get_all_customer_names(self):
        """Obtiene todos los nombres de los clientes."""
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT nombre FROM clientes"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [row[0] for row in rows]

    def get_customer_by_phone_number(self, phone_number: str) -> Customer:
        """Retrieve a customer by their phone number."""
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM clientes WHERE telefono = %s"
        cursor.execute(query, (phone_number,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Customer(row['cliente_id'], row['nombre'], row['telefono'], row['usuario_id'])
        return None