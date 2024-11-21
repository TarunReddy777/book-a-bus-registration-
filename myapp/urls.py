from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('findbus/', views.findbus, name='findbus'),
    path('bus_confirmation/', views.bus_confirmation, name='bus_confirmation'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('success/', views.success, name='success'),
    path('reserve_seat/', views.reserve_seat, name='reserve_seat'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('feedback/', views.feedback, name='feedback'),
    path('payment/', views.payment, name='payment'),
    path('select_seats/', views.select_seats, name='select_seats'),
    path('see_bookings/', views.see_bookings, name='see_bookings'),

    ##### ADMIN #####
    path('brsadmin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('brsadmin/manage_buses/', views.manage_buses, name='admin_manage_buses'),
    path('brsadmin/manage_drivers/', views.manage_drivers, name='admin_manage_drivers'),
    path('brsadmin/view_reservations/', views.view_reservations, name='admin_view_reservations'),
]
