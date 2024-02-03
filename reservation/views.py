from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation, Table


class MakeReservationView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation/reservation.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        reservation = form.save(commit=False)
        reservation.user = self.request.user

        conflicting_reservations = Reservation.objects.filter(
            table=reservation.table,
            start_date__lt=reservation.end_time,
            end_time__gt=reservation.start_date,
        )

        if conflicting_reservations.exists():
            messages.error(self.request, "Table is not available during the specified time range.")
            return render(self.request, 'reservation/reservation.html', {'form': form, 'tables': Table.objects.all()})
        elif reservation.number_of_persons > reservation.table.capacity:
            messages.error(self.request, "This table's capacity is less than the number of persons.")
            return render(self.request, 'reservation/reservation.html', {'form': form, 'tables': Table.objects.all()})
        else:
            reservation.save()
            messages.success(self.request, "Your table reserved successfully!")
            return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid form submission. Please check the form.")
        return render(self.request, 'reservation/reservation.html', {'form': form, 'tables': Table.objects.all()})


class AllReservationsView(ListView):
    model = Reservation
    template_name = 'reservation/view_reservations.html'
    context_object_name = 'user_reservations'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


@login_required
def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    if request.user == reservation.user:
        reservation.delete()
        messages.success(request, "Your reservation delete !")
        return redirect("reservation:view_reservations")
    return render(request, 'reservation/reservation')
