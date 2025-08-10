from django.urls import path
from . import views

urlpatterns = [
    path('reservations/', views.reservations_view, name='reservations'),
]



