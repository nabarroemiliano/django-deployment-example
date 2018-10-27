import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','users.settings')

import django
django.setup()


from users_list.models import User
from faker import Faker


fake_gen = Faker()


def populate(N=5):
    for entry in range(N):
        fake_name = fake_gen.name()
        fake_lastname = fake_gen.text()
        fake_email = fake_gen.email()

        us = User.objects.get_or_create(first_name = fake_name, last_name = fake_lastname, email = fake_email)[0]


if __name__=='__main__':
    print("Population begins!")
    populate(10)
    print("Population complete")
