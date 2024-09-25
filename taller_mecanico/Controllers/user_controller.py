from Services.user_service import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def verify_credentials(self, username, password):
        """Llamar al servicio para verificar si las credenciales son correctas."""
        return self.user_service.verify_credentials(username, password)