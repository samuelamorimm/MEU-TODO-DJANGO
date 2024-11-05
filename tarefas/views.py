from django.shortcuts import render, get_object_or_404, redirect

from tarefas.forms import TarefaForm
from .models import Tarefa

# Create your views here.
def tarefas(request):
    context = {'tarefas': Tarefa.objects.all(), 'form': TarefaForm(request.POST)}
    return render(request, 'index.html', context)

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TarefaForm()
    context = {'tarefas': Tarefa.objects.all(), 'form': TarefaForm(request.POST)}
    return render(request, 'index.html', context)

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect(tarefas)
    else:
        form = TarefaForm(instance=tarefa)
        
    return render(request, 'editar.html', {'tarefa': tarefa, 'form':form})

def deletar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect(tarefas)