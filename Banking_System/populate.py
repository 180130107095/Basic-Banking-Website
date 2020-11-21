import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Banking_System.settings')

import django
django.setup()

import random
from bankapp.models import User
from faker import Faker
fakegen = Faker()

def populate(N=10):
    for entry in range(N):
        fake_name = fakegen.name()
        fake_age = random.randint(18,100)
        fake_email = fakegen.email()
        fake_credit = fakegen.random_int()

        user = User.objects.get_or_create(name = fake_name, age = fake_age, email = fake_email, current_credit = fake_credit)

if __name__=='__main__':
    print("Populating data.. Please wait")
    populate()
    print("Complete")