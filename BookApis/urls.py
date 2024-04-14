
from django.urls import path
from .views import CreateBook, GetBooks, DeleteBook

urlpatterns = [
    path('create_book', CreateBook.as_view(), name="create_book"),
    path('get_books', GetBooks.as_view(), name="get_books"),
    path('delete_book/<int:pk>', DeleteBook.as_view(), name="delete_book" ),

]