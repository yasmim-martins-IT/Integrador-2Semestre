from django.contrib import admin
from .models import Ambiente , Sensores , Historico
#cria a página de admin que pode ser acessada atraves da página do administrador

admin.site.register(Ambiente)
admin.site.register(Sensores)
admin.site.register(Historico)

# Register your models here.
