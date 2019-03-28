from django.urls import path
from . import views

app_name = 'halls'

urlpatterns = [
    path('',views.HallListView.as_view(),name='hall_list'),
    path('hall/<int:pk>/',views.HallDetailView.as_view(),name='hall_detail'),
    path('hall/<int:pk>/hall_booked/',views.BookingView.as_view(),name='booking'),


]
