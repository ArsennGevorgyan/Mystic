from django.urls import path
from .views import MakeReservationView, cancel_reservation, AllReservationsView

app_name = "reservation"

urlpatterns = [
    path('reservation/', MakeReservationView.as_view(), name='reservation'),
    path('view-reservations/', AllReservationsView.as_view(), name='view_reservations'),
    path('cancel-reservation/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
]
