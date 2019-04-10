from django.contrib import admin

# Register your models here.
from .models import Creator, Presentation

admin.site.register(Creator)

admin.site.register(Presentation)