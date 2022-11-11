from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import TaskModel


# Create your views here.
class TaskList(ListView):
    template_name = 'list.html'
    model = TaskModel

class TaskDetail(DetailView):
    template_name = 'detail.html'
    model = TaskModel

class TaskCreate(CreateView):
    template_name = 'create.html'
    model = TaskModel
    fields = ('title','contact','category')
    success_url = reverse_lazy('list')

class TaskDelete(DeleteView):
    template_name = 'delete.html'
    model = TaskModel
    success_url = reverse_lazy('list')


class TaskUpdate(UpdateView):
    template_name = 'update.html'
    model = TaskModel
    fields = ('title','contact','category')
    success_url = reverse_lazy('list')