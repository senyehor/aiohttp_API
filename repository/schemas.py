from dataclasses import dataclass


@dataclass
class SchemaBase:
    id: int


@dataclass
class UserSchema(SchemaBase):
    email: str
    password: str


@dataclass
class LocationSchema(SchemaBase):
    name: str


@dataclass
class DeviceSchema(SchemaBase):
    type: str
    login: str
    password: str
    location: LocationSchema
    owner: UserSchema
