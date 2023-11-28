from django.urls import path
from .views import ListBook, CreateBook , InspectBook

urlpatterns = [
path('', ListBook.as_view(), name='home'),
path('create_book', CreateBook.as_view(), name='create_book'),
path('inspect_book', InspectBook.as_view(), name='inspect_book'),

]