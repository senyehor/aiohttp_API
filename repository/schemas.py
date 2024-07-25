from dataclasses import dataclass


@dataclass
class UserSchema:
    id: int
    email: str
    password: str


@dataclass
class DeviceSchema:
    id: int
    type: str
    login: str
    password: str
    location_id: int
    api_user_id: int


@dataclass
class LocationSchema:
    id: str
    name: str
