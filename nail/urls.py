from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view()),
    path('reservation/', views.ReserationView.as_view(), name='reserv_form'),
    path('<slug:slug>/', views.Services.as_view(), name='services'),
    path('page/booking/', views.Booking, name='booking'),
    path('page/contacts/', views.contacts, name='booking'),
    path('page/about/', views.about),

]