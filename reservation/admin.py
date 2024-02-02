from django.contrib import admin
from reservation.models import Reservation, Table


admin.site.register(Reservation)
admin.site.register(Table)
