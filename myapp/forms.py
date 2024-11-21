from django import forms
from django.contrib.auth.models import User
from .models import Feedback, Reservation, Route
from .models import Bus, Driver


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_number', 'capacity', 'fare', 'name', 'company', 'route']


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'license_number', 'contact_info', 'age']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['bus', 'seat']

class FindBusForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['source', 'destination']