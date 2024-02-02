from django.db import models
from users.models import User


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number} - Capacity: {self.capacity}"


class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reserved_table')
    start_date = models.DateTimeField()
    end_time = models.DateTimeField()

    def cancel_reservation(self):
        self.delete()

    def __str__(self):
        return f"{self.name} {self.start_date}"
