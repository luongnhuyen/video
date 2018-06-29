from Models.service import Service
from random import randint, choice
from faker import Faker
import mlab

mlab.connect()

fake = Faker()

# print(fake.address())
for i in range(50):
    print("Saving service", i+ 1, "...")
    service = Service(name=fake.name(),
                        yob=randint(1999,2001),
                        gender=randint(0,1),
                        height=randint(150,190),
                        phone=fake.phone_number(),
                        address=fake.address(),
                        status=choice([True,False]),
                        description = choice(["ngoan hiền", "dễ thương", "lễ phép với gia đình"]),
                        measurements = randint(60,90))


    service.save()
