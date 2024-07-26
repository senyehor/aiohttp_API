from factory import Factory, LazyAttribute, Sequence
from faker import Faker

from repository.schemas import UserSchema

fake = Faker()


class UserFactory(Factory):
    class Meta:
        model = UserSchema

    id = Sequence(lambda n: n + 1)
    email = LazyAttribute(lambda _: fake.email())
    password = LazyAttribute(lambda _: fake.password())
