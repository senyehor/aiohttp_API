from random import choice

from factory import Factory, LazyAttribute, Sequence, SubFactory
from faker import Faker

from repository.schemas import DeviceSchema, LocationSchema, UserSchema

fake = Faker()


class UserFactory(Factory):
    class Meta:
        model = UserSchema

    id = Sequence(lambda n: n + 1)
    email = LazyAttribute(lambda _: fake.email())
    password = LazyAttribute(lambda _: fake.password())


class LocationFactory(Factory):
    class Meta:
        model = LocationSchema

    id = Sequence(lambda n: n + 1)
    name = LazyAttribute(lambda _: fake.address())


class DeviceFactory(Factory):
    class Meta:
        model = DeviceSchema

    id = Sequence(lambda n: n + 1)
    type = LazyAttribute(lambda _: choice(['smart_watch', 'smart_fridge', 'smart_lamp']))
    login = LazyAttribute(lambda _: fake.word())
    password = LazyAttribute(lambda _: fake.password())
    location: LocationFactory = SubFactory(LocationFactory)
    owner: UserFactory = SubFactory(UserFactory)
