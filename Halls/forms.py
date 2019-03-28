from django import forms
from .models import Hall_Booking
from django.forms.widgets import SelectDateWidget

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):


    class Meta():
        model = Hall_Booking

        fields = {'hall','requested_by','booking_required','slot'}


    booking_required=forms.DateField(
    widget=SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
)
