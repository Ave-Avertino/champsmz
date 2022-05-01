from django.contrib import admin
from .models import Ocupacao, Nomes, Idioma, Tipo_Usuario
# Register your models here.
# Register your models here.
class Idioma_Admin(admin.ModelAdmin):
    search_fields = ['nome', 'lingua']
    list_display = ['nome', 'lingua']
    list_filter = ['nome', 'lingua']
    class Meta:
        model = Idioma


admin.site.register(Idioma, Idioma_Admin)