from django.contrib import admin
from .models import Categoria, Usuario
from .models import Recetas

admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Recetas)
