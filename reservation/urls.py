from django.urls import path
from .views import CancelReservationView, MakeReservationView, AllReservationsView
app_name = "reservation"

urlpatterns = [
    path('reservation/', MakeReservationView.as_view(), name='reservation'),
    path('view-reservations/', AllReservationsView.as_view(), name='view_reservations'),
    path('cancel-reservation/<int:reservation_id>/', CancelReservationView.as_view(), name='cancel_reservation'),
]
