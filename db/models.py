import peewee
from peewee import CharField, ForeignKeyField

from db.connection import database


class BaseModel(peewee.Model):
    class Meta:
        database = database


class User(BaseModel):
    email = CharField(unique=True, index=True, null=False)
    password = CharField(null=False)


class Location(BaseModel):
    name = CharField(null=False)


class Device(BaseModel):
    type = CharField(null=False)
    login = CharField(null=False)
    password = CharField(null=False)
    location = ForeignKeyField(Location, backref='devices', null=False, on_delete='RESTRICT')
    owner = ForeignKeyField(User, backref='devices', null=False, on_delete='RESTRICT')
