from Models.vehicle_model import Vehicle
from Daos.vehicle_dao import VehicleDAO

class VehicleService:
    def __init__(self):
        self.vehicle_dao = VehicleDAO()
        pass

    def create_vehicle(self, vehicle: Vehicle):
        # Crear un nuevo vehículo
        if self.is_registration_exists(vehicle.registration):
            raise ValueError("Ya existe un vehiculo con esta matricula.")
        self.vehicle_dao.create_vehicle(vehicle)

    def get_vehicle_by_registration(self, registration: str) -> Vehicle:
        # Obtener un vehículo por su matrícula
        return self.vehicle_dao.get_vehicle_by_registration(registration)

    def update_vehicle(self, vehicle: Vehicle):
        # Actualizar la información de un vehículo
        self.vehicle_dao.update_vehicle(vehicle)

    def is_registration_exists(self, registration: str) -> bool:
        """Check if a vehicle with the given registration already exists."""
        vehicle = self.vehicle_dao.get_vehicle_by_registration(registration)
        return vehicle is not None

