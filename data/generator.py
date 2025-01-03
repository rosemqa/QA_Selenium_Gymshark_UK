import random
from dataclasses import dataclass
from faker import Faker

fake = Faker('en_GB')


@dataclass
class Address:
    firstname: str
    lastname: str
    address1: str
    address2: str
    city: str
    postal_code: str
    phone: str


def generated_address():
    return Address(
        firstname=fake.first_name_male(),
        lastname=fake.last_name_male(),
        address1=fake.street_address(),
        address2=fake.street_address(),
        city=fake.city(),
        postal_code=fake.postcode(),
        phone=f'+44{fake.random_number(10)}'
    )


def not_valid_phone_number():
    short_number = fake.random_number(random.randint(1, 9))
    long_number = fake.random_number(22)
    string = fake.word()
    return [short_number, long_number, string]
