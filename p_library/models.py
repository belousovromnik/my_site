from django.db import models  
from reader.models import Reader
  
class Author(models.Model):  
    full_name = models.TextField(max_length=100, unique=True, verbose_name='Имя автора')  
    birth_year = models.SmallIntegerField(verbose_name='Дата рождения автора')  
    country = models.CharField(max_length=2, verbose_name='Страна автора')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['full_name']


class PubHouse(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование издательства', unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
        ordering = ['name']


class Book(models.Model):  
    ISBN = models.CharField(max_length=13, verbose_name='ISBN')  
    title = models.TextField(verbose_name='Наименование книги')  
    description = models.TextField(verbose_name='Описание книги', null = True)  
    year_release = models.SmallIntegerField(verbose_name='Год издания', null = True)  
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    copy_count = models.IntegerField(default=1, verbose_name='Количество копий')
    ost_count = models.IntegerField(default=0, verbose_name='Остаток копий')
    price = models.DecimalField(max_digits = 10, decimal_places=2, default=0, verbose_name='Цена')
    pubhouse = models.ForeignKey(PubHouse, on_delete=models.CASCADE, 
        verbose_name='Издательство', blank=True, 
        related_name="books", related_query_name="book")
    readers = models.ManyToManyField(
            Reader,
            through='Bookreader',
            through_fields=('book', 'reader'),
        )
    readers.empty_value_display = '-empty-'
    img = models.ImageField(upload_to='book', null=True, blank=True, verbose_name='Фото обложки')

    def __str__(self):
        return '{} - {} / {}'.format(self.author, self.title, self.ISBN)

    class Meta:
            verbose_name = 'Книга'
            verbose_name_plural = 'Книги'
            ordering = ['title']

class Bookreader(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=100, verbose_name='Комментарий', null=True, blank=True)  
    dataout = models.DateField(auto_now_add=True, null=True)
    datain = models.DateField(null=True)
