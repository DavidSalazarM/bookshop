from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('books/', views.books_list),
    path('books/<int:pk>/', views.book_detail,name='book'),
    path('download/<int:pk>/', views.download,name='download'),
]