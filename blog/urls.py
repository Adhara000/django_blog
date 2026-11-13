from django.urls import path
from . import views

urlpatterns = [
    
    #Rota para a pagina inicial
    path('', views.home, name='home'),

    #Rota para pagina de contatos
    path('contacts/', views.contacts, name='contacts'),
]