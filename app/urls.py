
from django.contrib import admin
from django.urls import path
from app.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', ClienteGenericsList.as_view()),
    path('clientes/<int:pk>/', ClienteGenericsRUD.as_view()),
    path('funcionarios/', FuncionarioGenericsList.as_view()),
    path('funcionarios/<int:pk>/', FuncionarioGenericsRUD.as_view()),
    path('servicos/', ServicoGenericsList.as_view()),
    path('servicos/<int:pk>/', ServicoGenericsRUD.as_view()), 
    path('atendimento/', AtendimentoGenericsList.as_view()),
    path('atendimento/<int:pk>/', AtendimentoGenericsRUD.as_view())
]
