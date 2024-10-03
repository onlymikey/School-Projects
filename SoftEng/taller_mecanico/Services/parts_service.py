from Models.parts_model import Parts
from Daos.parts_dao import PartsDAO

class PartsService:
    def __init__(self):
        self.parts_dao = PartsDAO()
        pass

    def create_parts(self, parts: Parts):
        # Crear una nueva parte
        self.parts_dao.create_parts(parts)

    def get_parts_by_id(self, partid: int) -> Parts:
        # Obtener una parte por su id
        return self.parts_dao.get_parts_by_id(partid)

    def get_parts_by_name(self, name: str) -> Parts:
        # Obtener una parte por su nombre
        return self.parts_dao.get_parts_by_name(name)

    def update_parts(self, parts: Parts):
        # Actualizar la información de una parte
        self.parts_dao.update_parts(parts)

    def get_all_parts_names(self):
        # Obtener todos los nombres de las partes
        return self.parts_dao.get_all_parts_names()

