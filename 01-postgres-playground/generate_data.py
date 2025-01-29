from faker import Faker
from dataclasses import dataclass
import random
import pandas as pd

fake = Faker()

# print(dir(fake))


@dataclass
class Person:
    name: str
    age: int
    email: str

    # job: str
    # company: str
    # company_email: str
    # adress: str
    # height: float


persons = [
    Person(name=fake.name(), age=random.randint(1, 100), email=fake.email())
    for _ in range(10)
]

print(persons)

df = pd.DataFrame(persons)

print(df)
