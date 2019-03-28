from django.db import models
from accounts.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()

# Create your models here.
class Hall(models.Model):
    hall_choice=[('Small',"50 People"),('Medium',"100 People"),('Large',"ABove 100 People")]
    name = models.CharField(max_length=264)
    hall_type = models.CharField(choices=hall_choice,max_length=264,default=None)
    vacant = models.BooleanField(default=False)
    particulars = models.TextField(null=True)
    image = models.ImageField(null=True,upload_to='media/HallPics/')
    # booked_on = models.TextField(null=True,default=None)

    def __str__(self):
        return self.name


    def approve_bookings(self):
        # self.booked_on = self.booked_on + self.bookings.booking_required

        return self.bookings.filter(approved_bookings=True)


class Hall_Booking(models.Model):
    hall_choicee=[('Morning',"9am-11:15"),('Break',"1:15"),('Evening',"3pm-5pm")]
    slot = models.CharField(choices=hall_choicee,max_length=264,default=None)

    hall = models.ForeignKey(Hall,related_name='bookings',on_delete=models.CASCADE,default=None)
    requested_on = models.DateTimeField(default=timezone.now())
    requested_by = models.OneToOneField(User,blank=True,on_delete=models.CASCADE,null=True,default=None)
    booking_required = models.DateField(blank=False)
    approved_bookings = models.BooleanField(default=False)

    def approve(self):
        self.approved_bookings = True
        self.save()


    def get_absolute_url(self):
        return reverse('halls:hall_list')
