from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('findbus/', views.findbus, name='findbus'),
    path('bus_confirmation/', views.bus_confirmation, name='bus_confirmation'),
    path('seebookings/', views.seebookings, name='seebookings'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('success/', views.success, name='success'),
    path('reserve_seat/', views.reserve_seat, name='reserve_seat'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('feedback/', views.feedback, name='feedback'),
    path('payment/', views.payment, name='payment'),
]
