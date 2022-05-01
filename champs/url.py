from django.urls import path, re_path
from champs import views

urlpatterns = [
    path(r'', views.inicio, name='inicio'),
]