from django.urls import path
from . import views

urlpatterns = [
    
    #Rota para a pagina inicial
    path('', views.home, name='home'),
]