from django.contrib import admin
from .models import cliente
from .models import cuenta
from .models import cuadro
# Register your models here.
admin.site.register(cliente)
admin.site.register(cuenta)
admin.site.register(cuadro)