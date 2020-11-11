from django.contrib import admin
from django import forms

from .models import Header, Reserv, Services, PriceList, Pages
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class PagesAdminForm(forms.ModelForm):
    content = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Pages
        fields = '__all__'



class PricelistInLine(admin.TabularInline):
    model = PriceList
    extra = 1

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)

@admin.register(Reserv)
class ReservAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'create_time', 'time', 'description',)

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines =[PricelistInLine,]
    ordering = ('id',)

@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cash',)

@admin.register(Pages)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    form = PagesAdminForm