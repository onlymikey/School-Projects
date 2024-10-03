from Models.customer_model import Customer
from Daos.customer_dao import CustomerDAO

class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDAO()
        pass

    def create_customer(self, customer: Customer):
        # Insertar el cliente en la base de datos
        if self.is_phone_number_exists(customer.phone):
            raise ValueError("Ya existe un cliente con este numero de telefono.")
        self.customer_dao.save_customer(customer)

    def is_phone_number_exists(self, phone_number: str) -> bool:
        """Check if a customer with the given phone number already exists."""
        customer = self.customer_dao.get_customer_by_phone_number(phone_number)
        return customer is not None

    def get_customer(self, customer_id):
        # Obtener el cliente desde la base de datos
        customer = self.customer_dao.get_customer_by_id(customer_id)
        if customer:
            return customer
        return None

    def update_customer(self, customer: Customer):
        # Obtener el cliente actual
        existing_customer = self.customer_dao.get_customer_by_id(customer.id)
        if not existing_customer:
            raise ValueError("Customer not found")
        self.customer_dao.update_customer(customer)

    def get_customer_by_name(self, name):
        return self.customer_dao.get_customer_by_name(name)

    def get_all_customer_names(self):
        return self.customer_dao.get_all_customer_names()