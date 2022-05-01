from django.urls import path
from contas import views
urlpatterns = [
    #path(r'', views.home, name='home'),
    path(r'', views.iniciar_sessao, name='iniciar'),
    path(r'login/<lingua>/', views.iniciar_sessao, name='iniciar_sessao'),
    path(r'logout/<lingua>/', views.terminar_sessao, name='terminar_sessao'),
    path(r'criar_conta/<lingua>/', views.criar_conta, name='criar_conta'),
]