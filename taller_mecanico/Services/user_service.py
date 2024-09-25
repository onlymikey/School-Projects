from Models.user_model import User
from Daos.user_dao import UserDAO

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()
        pass

    def create_user(self, user: User):
        # Insertar el usuario en la base de datos
        self.user_dao.create_user(user)

    def get_user(self, user_id):
        # Obtener el usuario desde la base de datos
        user = self.user_dao.get_user_by_id(user_id)
        if user:
            return user
        return None

    def update_user(self, user: User):
        # Obtener el usuario actual
        existing_user = self.user_dao.get_user_by_id(user.id)
        if not existing_user:
            raise ValueError("User not found")
        self.user_dao.update_user(user)

    def delete_user(self, user_id):
        # Eliminar el usuario de la base de datos
        self.user_dao.delete_user(user_id)

    def list_users(self):
        # Obtener todos los usuarios desde la base de datos
        users_data = self.user_dao.get_all_users()
        return [User(**data) for data in users_data]
    
    def verify_credentials(self, username, password):
        """Verificar si el username y password existen en la base de datos."""
        return self.user_dao.verify_user(username, password)
