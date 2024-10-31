from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_professores/', views.lista_professores, name='lista_professores'),
    path('cria_professores/', views.cria_professores, name='cria_professores'),
    path('atualiza_professores/<int:id>/', views.atualiza_professores, name='atualiza_professores'),
    path('deleta_professores/<int:id>/', views.deleta_professores, name='deleta_professores'),
    path('lista_alunos/', views.lista_alunos, name='lista_alunos'),
    path('cria_alunos/', views.cria_alunos, name='cria_alunos'),
    path('atualiza_alunos/<int:id>/', views.atualiza_alunos, name='atualiza_alunos'),
    path('deleta_alunos/<int:id>/', views.deleta_alunos, name='deleta_alunos'),
]
