import datetime
import sqlite3
import random
from faker import Faker
from django.utils import timezone

INSERT_ROUTE_QUERY = "INSERT INTO myapp_route (source, destination, startTime, endTime, distance) VALUES (?, ?, ?, ?, ?)"
INSERT_BUS_COMPANY_QUERY = "INSERT INTO myapp_buscompany (name, email) VALUES (?, ?)"
INSERT_DRIVER_QUERY = "INSERT INTO myapp_driver (name, license_number, contact_info, age) VALUES (?, ?, ?, ?)"
INSERT_BUS_QUERY = "INSERT INTO myapp_bus (bus_number, capacity, fare, name, company_id, route_id, driver_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
INSERT_PASSENGER_QUERY = "INSERT INTO myapp_passenger (name, user_id, phone_number, email) VALUES (?, ?, ?, ?)"
INSERT_SEAT_QUERY = "INSERT INTO myapp_seat (bus_id, seat_number, is_available) VALUES (?, ?, ?)"

UPDATE_ROUTE_QUERY = "UPDATE myapp_route SET source = ?, destination = ? WHERE id = ?"

# Replace 'your_database.sqlite3' with your actual database file
conn = sqlite3.connect('bus_reservation.sqlite3')
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
        startTime = timezone.now() + timezone.timedelta(minutes=random.randint(-60, 120)
                                                        )  # Randomize within 2 hours
        endTime = startTime + timezone.timedelta(hours=random.randint(
            1, 4), minutes=random.randint(0, 59))  # Random duration 1-4 hours
        # Random distance between 10 and 500 km
        distance = round(random.uniform(10.00, 500.00), 2)

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


def generate_buses(num_routes=20):
    buses = []
    for _ in range(num_routes):
        number = fake.vin()
        capacity = fake.random_number(digits=2)
        fare = fake.random_number(digits=3)
        name = fake.name()

        company = random.randint(1, 10)
        route = random.randint(1, 10)
        driver = random.randint(1, 10)

        seat_count = random.randint(40, 60)

        result = (number, capacity, fare, name,
                  company, route, driver, seat_count)
        buses.append(result)

    cursor.executemany(INSERT_BUS_QUERY, buses)
    conn.commit()
    cursor.close()


def generate_passengers(num_routes=3):
    passengers = []
    count = 1
    for _ in range(num_routes):
        name = fake.name()
        user_id = count
        phone_number = fake.phone_number()
        email = fake.email()

        result = (name, user_id, phone_number, email)
        passengers.append(result)
        count += 1
    cursor.executemany(INSERT_PASSENGER_QUERY, passengers)
    conn.commit()
    cursor.close()


def generate_seats(num_routes=10):
    seats = []
    for _ in range(num_routes):
        bus = random.randint(1, 10)
        seat_number = str(fake.random_number(digits=3, fix_len=3))
        is_available = True if random.randint(1, 1000) % 2 == 0 else False

        result = (bus, seat_number, is_available)
        seats.append(result)
    cursor.executemany(INSERT_SEAT_QUERY, seats)

    conn.commit()
    cursor.close()


def update_routes():
    options = [
        'Atlanta',
        'New York',
        'Los Angelos',
        'Tampa',
        'Carolina',
        'Washington DC',
        'San Francisco',
    ]

    count=1
    i = 0
    j = 1

    while(i<len(options) and j<len(options)):
        if count<=10:
            source = options[i]
            destination = options[j]
            row = (source, destination, count)
            cursor.execute(UPDATE_ROUTE_QUERY, row)
            count+=1
    
        else:
            source = options[i]
            destination = options[j]
            startTime = timezone.now() + timezone.timedelta(minutes=random.randint(-60, 120))  # Randomize within 2 hours
            endTime = startTime + timezone.timedelta(hours=random.randint(1, 4),
                                                     minutes=random.randint(0, 59))  # Random duration 1-4 hours
                # Random distance between 10 and 500 km
            distance = round(random.uniform(10.00, 500.00), 2)
            result = (source, destination, startTime, endTime, distance)
            cursor.execute(INSERT_ROUTE_QUERY, result)
        
        j += 1
        if j >= len(options):
            i += 1
            if i>=len(options):
                break
            j = i+1

    conn.commit()
    cursor.close()

update_routes()
