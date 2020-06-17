from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Content
from django.urls import reverse_lazy

# Create your views here.
class JokesListView(ListView):
    template_name = 'list.html'
    model = Content

class JokesDetailsView(DetailView):
    template_name = 'details.html'
    model = Content

class JokesCreateView(CreateView):
    template_name = 'new.html'
    model = Content
    fields = ['title', 'author', 'body']

class JokesUpdateView(UpdateView):
    template_name = 'update.html'
    model = Content
    fields = ['title', 'body']

class JokesDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Content
    success_url = reverse_lazy('list')
