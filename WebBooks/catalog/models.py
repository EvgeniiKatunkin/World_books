from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Input the genre of the book",
                            verbose_name="The book genre")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Input the language of the book",
                            verbose_name="The language of the book")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Input the author's first name",
                                  verbose_name="First name")
    last_name = models.CharField(max_length=100, help_text="Input the author's last name",
                                 verbose_name="Last name")
    date_of_birth = models.DateField(help_text="Input the author's birthdate",
                                     verbose_name="Date of birth", null=True, blank=True)
    date_of_death = models.DateField(help_text="Input the author's date of death",
                                     verbose_name="Date of death", null=True, blank=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Input the name of the book",
                             verbose_name="Name of the book")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              help_text="Choose a genre for the book",
                              verbose_name="Genre of the book", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 help_text="Choose the language of the book",
                                 verbose_name="Language of the book", null=True)
    author = models.ManyToManyField('Author', help_text="Choose the author of the book",
                                    verbose_name="Author of the book", null=True)
    summary = models.TextField(max_length=1000, help_text="Input a short description of the book",
                               verbose_name="Book annotation")
    isbn = models.CharField(max_length=13, help_text="No longer than 13 symbols",
                            verbose_name="ISBN of the book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Return URL-address for access to the certain specimen of a book
        return reverse('book-detail', args=[str(self.id)])
