from django import forms
from django.forms import ModelForm
from .models import Reserv

class ReservForm(ModelForm):
    class Meta:
        model = Reserv
        fields = ('name', 'phone', 'time', 'description',)