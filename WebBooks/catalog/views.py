from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Author, Book, BookInstance, Genre


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4


class BookDetailView(generic.DetailView):
    model = Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


def index(request):
    # Amount of books
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (in stock)
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    # Authors
    num_authors = Author.objects.count()

    # Amount of attendances
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'catalog/index.html', context={'num_books': num_books,
                                                          'num_instances': num_instances,
                                                          'num_instances_available': num_instances_available,
                                                          'num_authors': num_authors,
                                                          'num_visits': num_visits})


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Universal class of books in current user's order list.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
