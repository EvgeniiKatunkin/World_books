from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    # Generation amount of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = "stored")
    # The method 'all()' is applied by default
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    # Authors of books
    num_authors = Author.objects.count()

    # Creating index.html with data inside context
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_available': num_instances_available,
                           'num_authors': num_authors,
                           # 'num_visits': num_visits},
                           }
                  )


class BookListView(generic.ListView):
    model = Book
