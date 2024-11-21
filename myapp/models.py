from django.utils import timezone
import uuid
from django.db import models
from django.contrib.auth.models import User

class BusCompany(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Bus(models.Model):
    bus_number = models.CharField(max_length=20, unique=True)
    capacity = models.SmallIntegerField()
    fare = models.BigIntegerField()
    name = models.CharField(max_length=20)

    company = models.ForeignKey('BusCompany', on_delete=models.CASCADE, related_name="buses")
    route = models.ForeignKey('Route', on_delete=models.CASCADE, related_name="buses")
    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_buses")

    # seat_count = models.IntegerField()

    def __str__(self):
        return f"{self.bus_number} - {self.company.name}"

class Route(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    startTime = models.TimeField(default=timezone.now)
    endTime = models.TimeField(default=timezone.now)
    distance = models.DecimalField(max_digits=5, decimal_places=2,blank=True)

    def __str__(self):
        return f"{self.source} to {self.destination}"

class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20)
    contact_info = models.CharField(max_length=100)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.name

class Passenger(models.Model):
    name = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Seat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="seats")
    seat_number = models.CharField(max_length=5)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Seat {self.seat_number} on {self.bus.bus_number}"

class Reservation(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Booked', 'Booked'), ('Cancelled', 'Cancelled')])

class Ticket(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=20, default=uuid.uuid4)
    issue_date = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'),('Pending', 'Pending')])

class FeedBackRating(models.IntegerChoices):
    EXTREMELY_UNSATISFIED = 0, 'Poor'
    UNSATISFIED = 1, 'Bad'
    NORMAL = 2, 'Normal'
    SATISFIED = 3, 'Good'
    EXTREMELY_SATISFIED = 5, 'Excellent'

class Feedback(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.IntegerField(default=FeedBackRating.EXTREMELY_UNSATISFIED, choices=FeedBackRating.choices)
    submitted_at = models.DateTimeField(auto_now_add=True)
