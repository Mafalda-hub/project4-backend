from django.contrib import admin
from .models import *
# Register your models here.

class TattooAdmin(admin.ModelAdmin):
  list_display = ('name', 'description', 'categories')


admin.site.register(Tattoo)
admin.site.register(Artist)
admin.site.register(Category)