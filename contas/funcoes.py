from django.conf import settings
from django.contrib.auth import get_user_model
from .criptografia import Mistura as mst
from django.contrib.auth.models import User as usr
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Perfil, Email_Ativacao as ea, Senha_Redefinir
from idioma import idioma

User = get_user_model()

class contas:

    def verificacao_de_usuario(self, usuario, lingua='universal'):
        user_count = usr.objects.filter(username=usuario).count()
        idm = idioma.contas(lingua)
        existe = 0
        if (user_count > 0):
            existe = 0
        elif (user_count == 0):
            existe = 1
        context = {
            'idm_geral': idm[0],
            'idm_contas': idm[1],
            'lingua': lingua,
            'existe': existe,
        }
        return context

    def verificacao_de_senhas(self, senha1, senha2, lingua='universal'):
        idm = idioma.contas(lingua);
        igual = 0;
        if (senha1 != senha2):
            igual = 0
        elif (senha1 == senha2):
            igual = 1
        context = {
            'idm_geral': idm[0],
            'idm_contas': idm[1],
            'lingua': lingua,
            'igual': igual,
        }
        return context

    def verificacao_de_email(self, email, lingua='universal'):
        idm = idioma.contas(lingua)
        existe = 0
        user_count = usr.objects.filter(email=email).count()
        if (user_count == 0):
            existe = 1
        context = {
            'idm_geral': idm[0],
            'idm_contas': idm[1],
            'lingua': lingua,
            'existe': existe,
        }
        return context

    def activar_email(self, temp, subject, recipiente, tipo):
        url_de_ativacao = 'http://127.0.0.1:8000/accounts/'+str(tipo)+'/%s' % (temp)
        context = {
            'senha_de_ativacao': temp,
            'url_de_ativacao': url_de_ativacao,
        }
        mensagem = render_to_string('accounts/activation_message.txt', context)
        try:
            send_mail(subject=subject, message=mensagem, from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[recipiente], fail_silently=False, auth_password=settings.EMAIL_HOST_PASSWORD)
            return 1
        except:
            return 0

    def salvar(self, usuario, email, senha, lingua='universal'):
        idm = idioma.contas(lingua)
        usuario = usr.objects.get_or_create(username=usuario, email=email, password=senha)
        id = usr.objects.get(username=usuario)
        perfil = Perfil.objects.get_or_create(email=id.email, genero=5)
        try:
            temp = '' + str(mst.mistura(self)) + str(id.email)
            ativa = ea.objects.get_or_create(usuario=id, email_cod=temp, ativo=False)
            self.activar_email(temp, 'Activation Code', id.email, 'ativacao_email')
            print('Dados adicionados com sucesso!')
            return 1
        except:
            print('Ocorreu um erro ao adicionar dados na base de dados de activação!')
            return 0

    def definir_perfil(self, usuario, cont_pri, cont_sec, cont_ter, telemovel, aniversario, ocupacao, genero, passatempos, info='nada'):
        try:
            row = Perfil.objects.get(usuario=usuario)
            try:
                row.telemovel = telemovel;
                row.save()
            except:
                pass
            try:
                row.aniversario = aniversario;
                row.save()
            except:
                pass
            try:
                row.ocupacao = ocupacao;
                row.save()
            except:
                pass
            try:
                row.genero = genero;
                row.save()
            except:
                pass
            try:
                row.contacto_pri = cont_pri
                row.save()
            except:
                pass
            try:
                row.contacto_sec = cont_sec
                row.save()
            except:
                pass
            try:
                row.contacto_ter = cont_ter
                row.save()
            except:
                pass

            return 1
        except:
            print('Ocorreu um erro quando os dados estavam sendo gravados')
            return 0