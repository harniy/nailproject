from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import ReservForm
from .models import Header, Services, Pages


class Home(ListView):
    model = Header
    template_name ='site/base.html'




class Services(DetailView):
    model = Services
    slug_field = 'url'
    template_name = 'site/services.html'




class ReserationView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ReservForm(request.POST)

            if form.is_valid():
                form.save()
            return render(request, 'site/reservation.html')


def Booking(request):
    reserv = Pages.objects.filter(id=2)
    context = {'reserv': reserv}
    return render(request, 'site/booking.html', context)

def contacts(request):
    contacts = Pages.objects.filter(id=3)
    context= {'contacts': contacts}
    return render(request, 'site/contacts.html', context)

def about(request):
    about = Pages.objects.filter(id=4)
    context = {'about': about}
    return render(request, 'site/about.html', context)

