from Models.customer_model import Customer
from Daos.customer_dao import CustomerDAO

class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDAO()
        pass

    def create_customer(self, customer: Customer):
        # Insertar el usuario en la base de datos
        self.customer_dao.save_customer(customer)

    def get_customer(self, customer_id):
        # Obtener el usuario desde la base de datos
        customer = self.customer_dao.get_customer_by_id(customer_id)
        if customer:
            return customer
        return None

    def update_user(self, customer: Customer):
        # Obtener el usuario actual
        existing_customer = self.customer_dao.get_customer_by_id(customer.id)
        if not existing_customer:
            raise ValueError("Customer not found")
        self.customer_dao.update_customer(customer)

