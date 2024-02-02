from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView
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

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


class CancelReservationView(DeleteView):
    model = Reservation
    success_url = reverse_lazy('reservation:view_reservations')

    def post(self, request, *args, **kwargs):
        reservation = self.get_object()
        if request.user == reservation.user:
            reservation.delete()
            messages.success(request, "Your reservation has been canceled successfully!")
            return redirect("reservation:view_reservations")
        else:
            messages.error(request, "You do not have permission to cancel this reservation.")
            return redirect("reservation:view_reservations")
