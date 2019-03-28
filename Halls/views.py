from django.shortcuts import render
from django.views.generic import DetailView,ListView,CreateView
from .models import Hall,Hall_Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookingForm

from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
class HallDetailView(DetailView):
    model = Hall
    template_name = 'Halls/hall_detail.html'

class HallListView(ListView):
    model = Hall
    template_name = 'Halls/hall_list.html'


class BookingView(LoginRequiredMixin,CreateView):
    redirect_field_name = 'hall_detail.html'
    model = Hall_Booking
    form_class = BookingForm
    template_name = 'Halls/booking_form.html'


@login_required
def approve_booking(request,pk):
    hall_booked = get_object_or_404(Hall_Booking,pk=pk)
    hall_booked.approve()
    return redirect('hall_detail',pk=hall_booked.hall.pk)
