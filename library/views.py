from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from django.views.generic import ListView , CreateView , DetailView , UpdateView

# Create your views here.

class ListBook(ListView):
    model = Book
    template_name='library/home.html'

class CreateBook(CreateView):
    model=Book
    fields=['title' , 'author' , 'editorial' , 'published_date' , 'genre' , 'isbn' , 'resume' , 'front_page' , 'availability']
    template_name='library/create_book.html'
    success_url=reverse_lazy('home')

class InspectBook(DetailView):
    model=Book
    template_name='library/inspect_book.html'

# Listar, editar, detalles, borrar