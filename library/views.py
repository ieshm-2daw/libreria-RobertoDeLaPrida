from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from django.views.generic import ListView , CreateView , DetailView , UpdateView , DeleteView , UpdateView

# Create your views here.

class ListBook(ListView):
    model = Book
    template_name='library/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        available_books = Book.objects.filter(availability='A')
        unavailable_books = Book.objects.filter(availability='G')

        context['available_books'] = available_books
        context['unavailable_books'] = unavailable_books

        return context

    # def get_queryset(self):
    #     return Book.objects.filter(availability='A')

class CreateBook(CreateView):
    model=Book
    fields=['title' , 'author' , 'editorial' , 'published_date' , 'genre' , 'isbn' , 'resume' , 'front_page' , 'availability']
    template_name='library/create_book.html'
    success_url=reverse_lazy('home')

class InspectBook(DetailView):
    model=Book
    template_name='library/inspect_book.html'

class DeleteBook(DeleteView):
    model = Book
    template_name='library/delete_book.html'


class EditBook(UpdateView):
    model=Book
    fields=['title' , 'author' , 'editorial' , 'published_date' , 'genre' , 'isbn' , 'resume' , 'front_page' , 'availability']
    template_name=('library/edit_book.html')
    success_url=reverse_lazy('home')