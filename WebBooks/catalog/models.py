from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Input author's name", verbose_name="Author's name")
    last_name = models.CharField(max_length=100, help_text=" Input author's last name",
                                 verbose_name="Author's last name")
    date_of_birth = models.DateField(help_text="Input date of birth", verbose_name="Date of birth", null=True,
                                     blank=True)
    date_of_death = models.DateField(help_text="Input date of death", verbose_name="Date of death", null=True,
                                     blank=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Input title", verbose_name="Title")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text="Choose the genre", verbose_name="Genre",
                              null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text="Choose the language",
                                 verbose_name="Language", null=True)
    author = models.ManyToManyField('Author', help_text="Choose the author", verbose_name="Author")
    summary = models.TextField(max_length=1000, help_text="Input the book description", verbose_name="Annotation")
    isbn = models.CharField(max_length=13, help_text="Should be 13 symbols", verbose_name="ISBN of the book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True, help_text="Input the inventory number of the book",
                               verbose_name="Inventory number")
    imprint = models.CharField(max_length=200, help_text="Input publisher and year of release",
                               verbose_name="Publisher")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, help_text="Change condition of the book",
                               verbose_name="Status")
    due_back = models.DateField(null=True, blank=True, help_text="Input the end date of the status",
                                verbose_name="End status date")

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text=" Input book genre", verbose_name="Book genre")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, help_text=" Input book language", verbose_name="Book language")

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Input book status", verbose_name="Book status")

    def __str__(self):
        return self.name
