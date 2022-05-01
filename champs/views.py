from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from idioma import idioma
from contas.models import Idioma
# Create your views here.
@csrf_protect
def inicio(request, lingua='universal'):
    template = 'index.html'
    idm = idioma.geral(lingua)
    context = {
        'idm_geral':idm[0],
        'lingua':lingua,
    }
    return render(request, template, context)
