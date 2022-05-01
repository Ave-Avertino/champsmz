from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Idioma(models.Model):
    nome = models.CharField(max_length=50)
    lingua = models.CharField(max_length=10, primary_key=True, default='universal')
    bandeira = models.ImageField(upload_to='idioma', blank=True, null=True)
    class Meta:
        db_table = 'idioma'
    def __str__(self):
        return str(self.lingua)

class Nomes(models.Model):
    nome = models.CharField(max_length=30, primary_key=True)
    class Meta:
        db_table = 'nomes'
    def __str__(self):
        return self.nome
#tipo_usuario: Utente, Medico, Admnistrador, Director, Enfermeiro, Tecnico de Laboratorio
class Tipo_Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    cod_lang = models.CharField(max_length=5, null=True, blank=True)
    nome = models.CharField(max_length=75)
    nivel = models.IntegerField()
    class Meta:
        db_table = 'tipo_de_usuario'
    def __str__(self):
        return str(self.nome)+'_'+str(self.id)
'''Default sera "Desconhecido"'''
class Ocupacao(models.Model):
    id = models.BigAutoField(primary_key=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    cod_lang = models.CharField(max_length=5, null=True, blank=True)
    nome = models.CharField(max_length=15)
    class Meta:
        db_table = 'ocupacao'
    def __str__(self):
        return str(self.nome)+'_'+str(self.id)

class Perfil(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    tipo_usuario = models.ManyToManyField(Tipo_Usuario, related_name='tipo_de_usuario')
    foto = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    aniversario = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=False)
    class Meta:
        db_table = 'perfil'
    def __str__(self):
        return str(self.usuario)

class Senha_Redefinir(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    senha_cod = models.CharField(max_length=100)
    codigo = models.CharField(max_length=8)
    class Meta:
        db_table = "senha_redefinir"
    def __str__(self):
        return str(self.usuario)

class Email_Ativacao(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    email_cod = models.CharField(max_length=100)
    codigo = models.CharField(max_length=8)
    ativo = models.BooleanField(default=False)
    class Meta:
        db_table = 'email_ativacao'
    def __str__(self):
        return str(self.usuario)
