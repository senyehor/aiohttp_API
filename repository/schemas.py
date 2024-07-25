from dataclasses import dataclass


@dataclass
class SchemaBase:
    id: int


@dataclass
class UserSchema(SchemaBase):
    email: str
    password: str


@dataclass
class DeviceSchema(SchemaBase):
    type: str
    login: str
    password: str
    location_id: int
    api_user_id: int


@dataclass
class LocationSchema(SchemaBase):
    name: str
