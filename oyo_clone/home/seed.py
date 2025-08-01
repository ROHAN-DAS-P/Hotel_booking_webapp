# from django.contrib.auth.models import User
# from accounts.models import *
# from faker import Faker
# fake = Faker()
# import random

# def createUser():
#     email = fake.email()
#     HotelVendor.objects.create(
#         email = email,
#         business_name = fake.name(),
#         username = email,
#         first_name = fake.name(),
#         phone_number = random.randint(1111111111, 9999999999)
#     )

# from random import choice
# def createHotel():
#     for i in range(100):
#         hotel_vendor = choice(HotelVendor.objects.all())
#         amenities = list(Ameneties.objects.all())
#         hotel = Hotel.objects.create(
#             hotel_name = fake.company(),
#             hotel_description = fake.text(),
#             hotel_slug = fake.slug(),
#             hotel_owner = hotel_vendor,
#             hotel_price = fake.random_number(digits=4) / 100.0,
#             hotel_offer_price = fake.random_number(digits=4) / 100.0,
#             hotel_location = fake.address(),
#             is_active = fake.boolean()

#         )
#         hotel.ameneties.set(amenities)

import os
import sys
import django
import random
from faker import Faker

# ✅ Set correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oyo_clone.settings')

# ✅ Add the base project path (hotel_booking) to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# ✅ Setup Django
django.setup()

# Now you can import models
from accounts.models import HotelVendor, Hotel, Ameneties

# ------------------- FAKE DATA GENERATOR -------------------
fake = Faker()

def create_vendor():
    email = fake.email()
    vendor = HotelVendor.objects.create(
        email=email,
        username=email,
        business_name=fake.company(),
        first_name=fake.first_name(),
        phone_number=random.randint(1111111111, 9999999999),
    )
    print(f"✅ Created vendor: {vendor.username}")
    return vendor

def create_hotels(num=10):
    vendors = list(HotelVendor.objects.all())
    if not vendors:
        print("⚠️ No vendors found. Creating one...")
        vendors.append(create_vendor())

    amenities_list = list(Ameneties.objects.all())
    if not amenities_list:
        print("⚠️ No amenities found. Please create some Ameneties in the DB before running this.")
        return

    for _ in range(num):
        vendor = random.choice(vendors)
        hotel = Hotel.objects.create(
            hotel_name=fake.company(),
            hotel_description=fake.text(max_nb_chars=200),
            hotel_slug=fake.slug(),
            hotel_owner=vendor,
            hotel_price=round(random.uniform(1000, 5000), 2),
            hotel_offer_price=round(random.uniform(800, 4000), 2),
            hotel_location=fake.address(),
            is_active=True,
        )
        hotel.ameneties.set(amenities_list)
        print(f"🏨 Hotel created: {hotel.hotel_name}")

# Run the script
if __name__ == '__main__':
    print("🚀 Seeding fake data...")
    create_vendor()
    create_hotels(50)
    print("✅ Done seeding.")
