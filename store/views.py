from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Book, Author, Publisher
from django.http import FileResponse
from django.core.paginator import Paginator
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import os
import uuid
from pathlib import Path
from django.core.files import File


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

def check_pdf(file):
    try:
        PdfReader(file)
        return True
    except:
        return False

def book_save(title,authors,publisher,published,foto,pdf_file):
        Book.objects.create(
        title = title,
        authors = authors,
        publisher = publisher,
        published = published,
        book_img = foto,
        pdf_file = pdf_file,
        )
        


@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = request.POST
        file = request.FILES
        author = None
        publisher = None
        pdf_file_path = file["pdf_file"].temporary_file_path()
        if data["author"]:
            try: 
                author = Author.objects.get(name = data["author"]) 
            except:
                author = Author.objects.create(name = data["author"])
        if data["publisher"]:
            try: 
                publisher = Publisher.objects.get(name = data["publisher"]) 
            except:
                publisher = Publisher.objects.create(name = data["publisher"])
        

        
        if check_pdf(pdf_file_path) == False:
            return render(request, 'book_create.html')

        try:
            foto = file["book_img"]
            book_save(data["title"],author,publisher,data["published"],foto,file["pdf_file"])        
        except:
            file_foto_path = "/tmp/{}.jpg".format(uuid.uuid4()) 
            image = convert_from_path(pdf_file_path, single_file=True)[0]
            image.save(file_foto_path, "JPEG")
            
            path = Path(file_foto_path)
            with path.open(mode='rb') as f:
                foto = File(f, name=path.name)
                book_save(data["title"],author,publisher,data["published"],foto,file["pdf_file"])

        return render(request, 'book_create.html')
    else:
        return render(request, 'book_create.html')


