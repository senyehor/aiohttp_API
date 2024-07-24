from dataclasses import dataclass


@dataclass
class APIUser:
    id: int
    email: str
    password: str


@dataclass
class Device:
    id: int
    type: str
    login: str
    password: str
    location_id: int
    api_user_id: int


@dataclass
class Location:
    id: str
    name: str
