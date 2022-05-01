from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Casos(models.Model):
    champs_id = models.CharField(max_length=9, primary_key=True)
    kit_id = models.CharField(max_length=6, blank=False, null=False)
    nida = models.FloatField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=False)
    atualiza = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'casos'
    def __str__(self):
        return str(self.champs_id)

class Tipo_Amostra(models.Model):
    nome = models.CharField(max_length=20, primary_key=True)#Sangue, LCR,
    data = models.DateTimeField(auto_created=True, auto_now_add=False)
    atualiza = models.DateTimeField(auto_now=True, auto_created=True)
    class Meta:
        db_table = 'tipo_amostras'
    def __str__(self):
        return str(self.nome)

class Specimen(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)#Aliquota de sangue para TAC
    codigo = models.CharField(max_length=4)#Exemplo: .005
    tipo_amostras = models.ForeignKey(Tipo_Amostra, to_field='nome', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_created=True, auto_now_add=False)
    atualiza = models.DateTimeField(auto_now=True, auto_created=True)
    class Meta:
        db_table = 'specimen'
    def __str__(self):
        return str(self.nome)

class Caixas(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)#nome da caixa será dado automaticamente: 'CHAMPS/COMSA'+'Specimen ID'+'Número da caixa'
    specimen_id = models.ForeignKey(Specimen, to_field='nome', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_created=True, auto_now_add=False)
    atualiza = models.DateTimeField(auto_now=True, auto_created=True)
    class Meta:
        db_table = 'caixas'
    def __str__(self):
        return str(self.nome)+'_'+str(self.id)

class Amostra_Original(models.Model):
    specimenid = models.CharField(max_length=10, primary_key=True)
    caso = models.ForeignKey(Casos, to_field='champs_id', on_delete=models.CASCADE)
    specimen = models.ForeignKey(Specimen, to_field='nome', on_delete=models.CASCADE)
    caixa = models.ForeignKey(Caixas, to_field='id', on_delete=models.CASCADE)
    posicao = models.PositiveSmallIntegerField()
    caixa_anterior = models.ForeignKey(Caixas, to_field='id', related_name='caixa_anterior', on_delete=models.CASCADE)
    posicao_anterior = models.PositiveSmallIntegerField()
    extraido = models.BooleanField(default=False)
    extracao_nr = models.PositiveSmallIntegerField(default=0)
    processado = models.BooleanField(default=False)
    acabou = models.BooleanField(default=False)
    acabou_nr = models.PositiveSmallIntegerField(default=0)
    amostra_perdida = models.BooleanField(default=False)
    reporte = models.TextField(blank=True, null=True)
    data_perdida_notificacao = models.DateField(auto_created=False, auto_now=False, auto_now_add=False)
    criado = models.DateTimeField(auto_created=True, auto_now_add=False)
    alterado = models.DateTimeField(auto_now=True,)
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        db_table = 'amostra_original'
    def __str__(self):
        return str(self.specimen_id)

#Por cada ID, só poderá permitir o máximo número de extrações da máquina
class Extracao_Ordem(models.Model):
    id = models.BigAutoField(primary_key=True)
    class Meta:
        db_table = 'extracao_ordem'
    def __str__(self):
        return str(self.id)

class DNA_Extraido(models.Model):
    specimenid = models.CharField(max_length=10, primary_key=True)
    dna_repetido = models.BooleanField(default=False)
    caso = models.ForeignKey(Casos, to_field='champs_id', on_delete=models.CASCADE)
    specimen = models.ForeignKey(Specimen, to_field='nome', on_delete=models.CASCADE)
    caixa = models.ForeignKey(Caixas, to_field='id', related_name='dna_caixa', on_delete=models.CASCADE)
    posicao = models.PositiveSmallIntegerField()
    extracao_ordem = models.ForeignKey(Extracao_Ordem, to_field='id', on_delete=models.CASCADE)
    ordem_extracao = models.PositiveSmallIntegerField()
    caixa_anterior = models.ForeignKey(Caixas, to_field='id', related_name='dna_caixa_anterior', on_delete=models.CASCADE)
    posicao_anterior = models.PositiveSmallIntegerField()
    repetir = models.BooleanField(default=False)
    processado = models.BooleanField(default=False)
    processado_nr = models.PositiveSmallIntegerField()#Se processar pela segunda vez, o repetir deve voltar ao False
    acabou = models.BooleanField(default=False)
    acabou_nr = models.PositiveSmallIntegerField(default=0)
    dna_perdido = models.BooleanField(default=False)
    reporte = models.TextField(blank=True, null=True)
    data_perdida_notificacao = models.DateField(auto_created=False, auto_now=False, auto_now_add=False)
    data = models.DateTimeField(auto_created=True, auto_now_add=False)
    atualiza = models.DateTimeField(auto_now=True, auto_created=True)
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        db_table = 'dna_extraido'
    def __str__(self):
        return str(self.specimen_id)