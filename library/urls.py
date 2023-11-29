from django.urls import path
from .views import ListBook, CreateBook , InspectBook, DeleteBook, EditBook

urlpatterns = [
path('', ListBook.as_view(), name='home'),
path('create_book', CreateBook.as_view(), name='create_book'),
path('inspect/<int:pk>', InspectBook.as_view(), name='inspect_book'),
path('delete_book',DeleteBook.as_view(), name='delete_book'),
path('edit/<int:pk>',EditBook.as_view(), name='edit_book'),
]