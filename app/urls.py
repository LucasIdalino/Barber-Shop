
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from app.views import *


router = routers.DefaultRouter()
router.register(r'funcionarios/', FuncionarioViewSet)
router.register(r'clientes/', ClienteModelViewSet)
router.register(r'servicos/', ServicoViewSet)
router.register(r'atendimentos/', AtendimentoViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
]


