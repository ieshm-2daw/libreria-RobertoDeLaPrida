import datetime
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render ,redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Book , Loan
from django.views.generic import ListView , CreateView , DetailView , UpdateView , DeleteView , UpdateView , View

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

class LoanBook(View):
    template_name = 'library/loan_book.html'
    def get(self,request,pk):
        book = Book.objects.get(id=pk)
        return render(request, self.template_name, {'book':book})
    
    def post(self,request,pk):
        book = get_object_or_404(Book, pk=pk)
        book.availability = 'G'
        book.given_date = datetime.datetime.now()
        book.save()
        return redirect('home')
    
class ReturnBook(View):
    template_name = 'library/return_book.html'
    def get(self,request,pk):
        book = Book.objects.get(id=pk)
        return render(request,self.template_name, {'book':book})
    
    def post(self,request,pk):
        book= get_object_or_404(Book, pk=pk)
        book.availability = 'A'
        book.save()
        return redirect('home')

class ListBookByUser(View):
    model = Loan
    template_name='library/list_book_by_name'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        available_books = Book.objects.filter(availability='A', user = self.request.user)
        unavailable_books = Book.objects.filter(availability='G', user = self.request.user)

        context['available_books'] = available_books
        context['unavailable_books'] = unavailable_books

        return context