from db.models import Device, Location, User
from repository.repositories.pee_wee_crud_repository import PeeWeeCRUDRepository


class UserPeeWeeRepository(PeeWeeCRUDRepository):
    model_class = User


class DevicePeeWeeRepository(PeeWeeCRUDRepository):
    model_class = Device


class LocationPeeWeeRepository(PeeWeeCRUDRepository):
    model_class = Location
