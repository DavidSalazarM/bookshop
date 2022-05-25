from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Book, Author, Publisher
from django.http import FileResponse
from django.core.paginator import Paginator

@csrf_exempt
def books_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        paginator = Paginator(books, 10) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'books_list.html', {"page_obj":page_obj})


@csrf_exempt
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return render(request, 'book_detail.html', {"book":book})

@csrf_exempt
def download(request, pk):
    obj = Book.objects.get(pk=pk)
    filepath = obj.pdf_file.path
    response = FileResponse(open(filepath, 'rb'),content_type='application/force-download')
    return response
