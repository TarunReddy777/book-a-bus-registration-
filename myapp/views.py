from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bus, Reservation, Route, Ticket, Passenger, Feedback, BusCompany, Seat, Payment
from .forms import FindBusForm, UserRegistrationForm, FeedbackForm, ReservationForm
from .models import Bus, User, BusCompany, Seat, Route, Driver
from django.core.cache import cache
import random

@login_required
def home(request):
    return render(request, 'myapp/home.html')

@login_required
def bus_confirmation(request):
    if request.method == 'POST':
        bus_number = request.POST.get('bus_number')
        from_route = request.POST.get('from_route')
        to_route = request.POST.get('to_route')
        date_of_journey = request.POST.get('date_of_journey')

        context = {
            'bus_number': int(bus_number),
            'from_route': from_route,
            'to_route': to_route,
            'date_of_journey': date_of_journey,
        }
        cache.set('booking_data', context)
        return render(request, 'myapp/bus_confirmation.html', context)

@login_required
def findbus(request):
    if request.method == 'POST':
        from_route = request.POST.getlist('source')[0]
        to_route = request.POST.getlist('destination')[0]
        date_of_journey = request.POST.get('date')

        # print(from_route, to_route, date_of_journey)
        buses = [
            {
                'bus_number': 1,
                'departure_time': '10:00 AM',
                'arrival_time': '05: 00 PM'
            },
            {
                'bus_number': 2,
                'departure_time': '11:00 AM',
                'arrival_time': '06: 00 PM'
            },
            {
                'bus_number': 3,
                'departure_time': '12:00 PM',
                'arrival_time': '07: 00 PM'
            },
            {
                'bus_number': 4,
                'departure_time': '01:00 PM',
                'arrival_time': '08: 00 PM'
            },
            {
                'bus_number': 5,
                'departure_time': '02:00 PM',
                'arrival_time': '09: 00 PM'
            },
            {
                'bus_number': 6,
                'departure_time': '03:00 PM',
                'arrival_time': '10: 00 PM'
            }
        ]
        context = {'buses': buses, 'from_route': from_route,
                   'to_route': to_route, 'date_of_journey': date_of_journey}
        return render(request, 'myapp/list_buses.html', context)

    context = {
        'options': [
            ('Atlanta', 'Atlanta'),
            ('New York', 'New York'),
            ('Los Angelos', 'Los Angelos'),
            ('Tampa', 'Tampa'),
            ('Carolina', 'Carolina'),
            ('Washington DC', 'Washington DC'),
            ('San Francisco', 'San Francisco')
        ]
    }
    return render(request, 'myapp/findbus.html', context=context)


def seebookings(request):
    return render(request, 'myapp/seebookings.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(username, email, password)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created Successfully!")
        return redirect('/signin/')
    else:
        form = UserRegistrationForm()
    return render(request, 'myapp/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('findbus')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'myapp/signin.html')


@login_required
def success(request):
    return render(request, 'myapp/success.html', {'user': request.user})


def signout(request):
    logout(request)
    return redirect('home')


@login_required
def reserve_seat(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.passenger = Passenger.objects.get(user=request.user)
            reservation.save()
            messages.success(request, "Reservation made successfully!")
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'myapp/reserve_seat.html', {'form': form})


@login_required
def reservation_success(request):
    return render(request, 'myapp/reservation_success.html')


@login_required
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'myapp/feedback.html', {'form': form})

@login_required
def payment(request):
    user = request.user
    booking_data = cache.get('booking_data')
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment = Payment.objects.create(amount=amount, method='Online', status='Paid')
        reservation = Reservation.objects.create(
            bus=Bus.objects.get(id=random.randint(1, 10)),
            route=Route.objects.get(id=random.randint(1,10)),
            passenger=Passenger.objects.get(id=random.randint(1,3)),
            seat=Seat.objects.get(id=random.randint(1, 10)),
            status="Booked"
        )
        context = {
            'reservation_id': reservation.id,
            'source': booking_data['from_route'],
            'destination': booking_data['to_route'],
            'date': booking_data['date_of_journey'],
            'bus_number': reservation.bus.bus_number,
            'distance': reservation.route.distance,
            'payment_amount': amount
        }
        return render(request, 'myapp/reservation_success.html', context=context)

    return render(request, 'myapp/payment.html', booking_data)




############# ADMIN ##############


# @login_required
def admin_dashboard(request):
    return render(request, 'myapp/admin_dashboard.html')


# @login_required
def manage_buses(request):
    buses = Bus.objects.all()
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New bus added successfully!")
            return redirect('admin_manage_buses')
    else:
        form = BusForm()
    return render(request, 'myapp/manage_buses.html', {'buses': buses, 'form': form})


# @login_required
def manage_drivers(request):
    drivers = Driver.objects.all()
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New driver added successfully!")
            return redirect('admin_manage_drivers')
    else:
        form = DriverForm()
    return render(request, 'myapp/manage_drivers.html', {'drivers': drivers, 'form': form})


# @login_required
def view_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'myapp/view_reservations.html', {'reservations': reservations})
