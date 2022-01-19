from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('store/', views.books_list),
    path('store/<int:pk>/', views.book_detail,name='book'),
]