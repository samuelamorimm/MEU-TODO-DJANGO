from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título da tarefa')
    situacao = models.BooleanField(default=False, verbose_name='Completa')

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return self.titulo

    