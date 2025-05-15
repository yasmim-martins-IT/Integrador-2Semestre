from django.contrib import admin
from .models import Ambiente , Sensores , Historico

admin.site.register(Ambiente)
admin.site.register(Sensores)
admin.site.register(Historico)

# Register your models here.
