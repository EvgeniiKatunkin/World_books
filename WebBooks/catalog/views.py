from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Book, BookInstance, Genre


def index(request):
    # Amount of books
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (in stock)
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    # Authors
    num_authors = Author.objects.count()

    return render(request, 'catalog/index.html', context={'num_books': num_books,
                                                          'num_instances': num_instances,
                                                          'num_instances_available': num_instances_available,
                                                          'num_authors': num_authors})
