from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User as usr
from django.http import JsonResponse
from django.http import Http404
from time import localtime
from django.contrib.auth import get_user_model
from idioma.idioma import contas as cnts
from .funcoes import contas
from contas.models import Idioma
from django.views.decorators.csrf import csrf_protect
#from rest_framework import viewsets
#from .serializadores import Passatempo_srl

@csrf_protect
# Create your views here.

def criar_conta(request, lingua='universal'):

    if(request.method=='POST'):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = request.POST.get('usuario')
        try:
            novo_usuario = usr.objects.filter(email=email).count()
            if(novo_usuario==0):
                novo_usuario = contas.salvar(usuario, email, senha, lingua)
        except:
            pass
    idm = cnts(lingua)
    template = 'signin.html'
    context = {
        'idm_geral': idm[0],
        'idm_contas': idm[1],
        'lingua': lingua,
        'tipo': 0,
    }
    return render(request, template, context)

def recuperar_senha(request, lingua='universal'):
    idm = cnts(lingua)
    template = 'login.html'
    context = {
        'idm_geral': idm[0],
        'idm_contas': idm[1],
        'lingua': lingua,
        'idioma': Idioma.objects.all(),
        'tipo': 0,
    }
    return render(request, template, context)

def iniciar_sessao(request, lingua='universal'):
    try:
        if(request.user.is_authenticated() == True):
            return HttpResponseRedirect('/home/' + lingua + '/')
    except:
        pass
    template = 'login.html'
    idm = cnts(lingua); condicao = 0
    print('Inicio method ajax '+str(request.is_ajax())+' and post-get is ',str(request.method))
    lang_temp = Idioma.objects.get(lingua=lingua); lang = []; idiomas = []
    lang.append(lang_temp.nome); lang.append(lang_temp.lingua)
    for i in Idioma.objects.all():
        idiomas.append([i.nome, i.lingua])
    if(request.is_ajax()==True):
        if request.method=='POST':
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            try:
                try:
                    usuario = usr.objects.get(email=email)
                    condicao = 3
                    print(type(usuario.username),' usuario',usuario.username)
                    login_sessao = auth.authenticate(request, username=usuario.username, password=senha)
                except:
                    usuario = usr.objects.get(username=email)
                    condicao = 3
                    login_sessao = auth.authenticate(request, username=usuario, password=senha)
                finally:
                    auth.login(request, login_sessao)
                print('Senha aceite')
                if (usuario.is_authenticated == True):
                    print('Redireciona a pagina de cursos')
                    condicao = 0
                else:
                    condicao = 2
            except:
                condicao = 1
    else:
        try:
            if(request.user.is_authenticated==True):
                return HttpResponseRedirect('/cursos/home/' + lingua + '/')
        except:
            pass
    context = {
        'idm_geral': idm[0],
        'idm_contas': idm[1],
        'lingua': lingua,
        'condicao': condicao,
        'idioma': idiomas,
        'lang': lang,
    }

    if request.is_ajax()==True:
        print('entrou no ajax positive')
        return JsonResponse(context)
    else:
        print('respondeu post')
        return render(request, template, context)

def terminar_sessao(request, lingua='universal'):
    print('Terminando a sessao')
    try:
        auth.logout(request)
        return HttpResponseRedirect('/')
    except:
        template = 'erro.html'
        idm = cnts(lingua)
        context = {
            'idm_geral': idm[0],
            'idm_contas': idm[1],
            'lingua': lingua,
        }
        return render(request, template, context)
