from django.http import response
from rest_framework.test import APITestCase
from .models import Author, Publisher, Book
import datetime


class BooksList(APITestCase):
    
    def test_get_books_list(self):            
        author = Author.objects.create(**{            
            'first_name': 'Argo',            
            'last_name': 'Zax' 
        })

        publisher = Publisher.objects.create(**{
            'name': 'Menelao',
            'city': 'Cebilla',
            'country': 'España'
        })

        book_1 = Book.objects.create(**{
            'title': 'Quijote',
            'authors': author,
            'publisher': publisher,
            'published': "1999-12-12",
        })

        book_2 =Book.objects.create(**{
            'title': 'Chascarrillo',
            'authors': author,
            'publisher': publisher,
            'published': "2000-12-12",
        })
        
        response = self.client.get('/bookshop/store/')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'books_list.html')

        books = Book.objects.all()
        self.assertEqual(len(books), 2)
        
        #book 1
        time = datetime.datetime.strptime(book_1.published, '%Y-%m-%d')
        book_1_published = time.strftime("%b. %d, %Y")

        
        self.assertContains(response, book_1.title)
        self.assertContains(response, book_1.authors.first_name + " " + book_1.authors.last_name)
        self.assertContains(response, book_1.publisher.name)
        self.assertContains(response, book_1_published)

        #book 2
        time = datetime.datetime.strptime(book_2.published, '%Y-%m-%d')
        book_2_published = time.strftime("%b. %d, %Y")

        self.assertContains(response, book_2.title)
        self.assertContains(response, book_2.authors.first_name + " " + book_1.authors.last_name)
        self.assertContains(response, book_2.publisher.name)
        self.assertContains(response, book_2_published)
    
class BookDetail(APITestCase):
    
    def test_get_one_book(self):

        author = Author.objects.create(**{            
            'first_name': 'Argo',            
            'last_name': 'Zax' 
        })

        publisher = Publisher.objects.create(**{
            'name': 'Menelao',
            'city': 'Cebilla',
            'country': 'España'
        })

        book_1 = Book.objects.create(**{
            'title': 'Quijote',
            'authors': author,
            'publisher': publisher,
            'published': "1999-12-12",
        })

        response = self.client.get('/bookshop/store/{}/'.format(book_1.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_detail.html')

        time = datetime.datetime.strptime(book_1.published, '%Y-%m-%d')
        book_1_published = time.strftime("%b. %d, %Y")

        self.assertContains(response, book_1.title)
        self.assertContains(response, book_1.authors.first_name + " " + book_1.authors.last_name)
        self.assertContains(response, book_1.publisher.name)
        self.assertContains(response, book_1_published)
    
    def test_try_get_book_not_exist(self):
        response = self.client.get('/bookshop/store/-1/')
        self.assertEqual(response.status_code, 404)


        
        
        






       


