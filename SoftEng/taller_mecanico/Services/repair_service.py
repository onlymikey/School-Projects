from Models.repair_model import Repair
from Daos.repair_dao import RepairDAO

class RepairService:
    def __init__(self):
        self.vehicle_dao = RepairDAO()
        pass

    def create_repair(self, repair: Repair):
        # Crear una nueva reparación
        self.vehicle_dao.create_repair(repair)

    def get_repair_by_id(self, id_repair: int) -> Repair:
        # Obtener una reparación por su id
        return self.vehicle_dao.get_repair_by_id(id_repair)

    def update_repair(self, repair: Repair):
        # Actualizar la información de una reparación
        self.vehicle_dao.update_repair(repair)