from django.contrib import admin
from .models import Casos, Tipo_Amostra, Specimen, Caixas, Amostra_Original, Extracao_Ordem, DNA_Extraido
# Register your models here.
# Register your models here.
class Casos_Admin(admin.ModelAdmin):
    search_fields = ['champs_id', 'kit_id', 'nida', 'data']
    list_display = ['champs_id', 'kit_id', 'nida', 'data']
    list_filter = ['champs_id', 'kit_id', 'nida', 'data']
    class Meta:
        model = Casos
# Register your models here.
class Tipo_Amostra_Admin(admin.ModelAdmin):
    search_fields = ['nome', 'data']
    list_display = ['nome', 'data']
    list_filter = ['nome', 'data']
    class Meta:
        model = Tipo_Amostra
# Register your models here.
class Specimen_Admin(admin.ModelAdmin):
    search_fields = ['nome', 'codigo', 'tipo_amostras','data']
    list_display = ['nome', 'codigo', 'tipo_amostras','data']
    list_filter = ['nome', 'codigo', 'tipo_amostras','data']
    class Meta:
        model = Specimen
# Register your models here.
class Caixas_Admin(admin.ModelAdmin):
    search_fields = ['nome', 'specimen_id','data']
    list_display = ['nome', 'specimen_id','data']
    list_filter = ['nome', 'specimen_id','data']
    class Meta:
        model = Caixas
# Register your models here.
class Amostra_Original_Admin(admin.ModelAdmin):
    search_fields = ['specimen_id', 'caso', 'caixa', 'posicao', 'caixa_anterior', 'extraido',
                     'processado', 'acabou', 'amostra_perdida', 'usuario']
    list_display = ['specimen_id', 'caso', 'caixa', 'posicao', 'caixa_anterior', 'extraido',
                     'processado', 'acabou', 'amostra_perdida', 'usuario']
    list_filter = ['specimen_id', 'caso', 'caixa', 'posicao', 'caixa_anterior', 'extraido',
                     'processado', 'acabou', 'amostra_perdida', 'usuario']
    class Meta:
        model = Amostra_Original
# Register your models here.
class Extracao_Ordem_Admin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id']
    list_filter = ['id']
    class Meta:
        model = Extracao_Ordem
# Register your models here.
class DNA_Extraido_Admin(admin.ModelAdmin):
    search_fields = ['specimen_id', 'dna_repetido', 'caso', 'caixa', 'posicao', 'caixa_anterior', 'repetir', 'processado',
                     'acabou', 'dna_perdido', 'usuario']
    list_display = ['specimen_id', 'dna_repetido', 'caso', 'caixa', 'posicao', 'caixa_anterior', 'repetir', 'processado',
                     'acabou', 'dna_perdido', 'usuario']
    list_filter = ['specimen_id', 'dna_repetido', 'caso', 'caixa', 'posicao', 'caixa_anterior', 'repetir', 'processado',
                     'acabou', 'dna_perdido', 'usuario']
    class Meta:
        model = DNA_Extraido

admin.site.register(Casos, Casos_Admin),
admin.site.register(Tipo_Amostra, Tipo_Amostra_Admin),
admin.site.register(Specimen, Specimen_Admin),
admin.site.register(Caixas, Caixas_Admin),
admin.site.register(Amostra_Original, Amostra_Original_Admin),
admin.site.register(Extracao_Ordem, Extracao_Ordem_Admin),
admin.site.register(DNA_Extraido, DNA_Extraido_Admin),