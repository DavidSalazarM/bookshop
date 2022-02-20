from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('books/', views.books_list),
    path('book/<int:pk>/', views.book_detail,name='book'),
]