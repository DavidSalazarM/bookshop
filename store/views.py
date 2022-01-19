from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Book, Author, Publisher

@csrf_exempt
def books_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'books_list.html', {"books":books})


@csrf_exempt
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return render(request, 'book_detail.html', {"book":book})
