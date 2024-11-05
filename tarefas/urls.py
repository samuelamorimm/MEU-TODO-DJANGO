from django.contrib import admin
from django.urls import path
from .views import tarefas, criar_tarefa, editar_tarefa, deletar_tarefa

urlpatterns = [
    path('', tarefas, name='tarefas'),
    path('criar/', criar_tarefa, name='criar_tarefa'),
    path('editar/<int:id>', editar_tarefa, name='editar_tarefa'),
    path('deletar/<int:id>', deletar_tarefa, name='deletar_tarefa'),
]
