from django.contrib import admin
from .models import Phonebook,User

# Register your models here.
admin.site.register(Phonebook)
admin.site.register(User)