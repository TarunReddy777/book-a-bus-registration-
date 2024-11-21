import datetime
import sqlite3
import random
from faker import Faker
from django.utils import timezone

INSERT_ROUTE_QUERY = "INSERT INTO myapp_route (source, destination, startTime, endTime, distance) VALUES (?, ?, ?, ?, ?)"
INSERT_BUS_COMPANY_QUERY = "INSERT INTO myapp_buscompany (name, email) VALUES (?, ?)"
INSERT_DRIVER_QUERY = "INSERT INTO myapp_driver (name, license_number, contact_info, age) VALUES (?, ?, ?, ?)"

conn = sqlite3.connect('bus_reservation.sqlite3')  # Replace 'your_database.sqlite3' with your actual database file
cursor = conn.cursor()
# # Commit the changes
# conn.commit()
# # Close the connection
# conn.close()
fake = Faker()

def generate_random_routes(num_routes=20):
    routes = []
    for _ in range(num_routes):
        source = fake.city()
        destination = fake.city()
        while source == destination:  # Ensure source and destination are different
            destination = fake.city()
        startTime = timezone.now() + timezone.timedelta(minutes=random.randint(-60, 120))  # Randomize within 2 hours
        endTime = startTime + timezone.timedelta(hours=random.randint(1, 4), minutes=random.randint(0, 59))  # Random duration 1-4 hours
        distance = round(random.uniform(10.00, 500.00), 2)  # Random distance between 10 and 500 km

        result = (source, destination, startTime, endTime, distance)
        routes.append(result)
    
    cursor.executemany(INSERT_ROUTE_QUERY, routes)
    conn.commit()
    cursor.close()


def generate_random_bus_company(num_routes=20):
    bus_company = []
    for _ in range(num_routes):
        name = fake.name()
        email = fake.email()
        
        result = (name, email)
        bus_company.append(result)
    
    cursor.executemany(INSERT_BUS_COMPANY_QUERY, bus_company)
    conn.commit()
    cursor.close()

def generate_driver_name(num_routes=20):
    drivers = []
    for _ in range(num_routes):
        name = fake.name()
        license_number = fake.random_number(digits=5, fix_len=5)
        contact_info = fake.address()
        dob = fake.date_of_birth(minimum_age=18, maximum_age=65)
        age = (datetime.date.today() - dob).days
        
        result = (name, license_number, contact_info, age)
        drivers.append(result)
    
    cursor.executemany(INSERT_DRIVER_QUERY, drivers)
    conn.commit()
    cursor.close()

generate_driver_name(10)