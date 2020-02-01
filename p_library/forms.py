from django import forms  
from p_library.models import Author, Book, Bookreader, PubHouse
from reader.models import Reader
  
class AuthorForm(forms.ModelForm):  

    full_name = forms.CharField(label='Автор',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите автора'}))
    birth_year = forms.IntegerField(label='Год рождения',
                           widget=forms.NumberInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите год рождения'}))
    country = forms.CharField(label='Страна',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите страну'}))
    
    class Meta:  
        model = Author  
        fields = '__all__'


class BookreaderForm(forms.ModelForm):
    book = forms.ModelChoiceField(label='Книга', queryset=Book.objects.all(),
                                       widget=forms.Select(
                                           attrs={'class': 'form-control',
                                                  'placeholder': 'Книга'}))
    reader = forms.ModelChoiceField(label='Читатель', queryset=Reader.objects.all(),
                                     widget=forms.Select(
                                         attrs={'class': 'form-control',
                                                'placeholder': 'Читатель'}))
    comment = forms.CharField(label='Комментарий',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Комментарий'}))

    class Meta(object):
        model = Bookreader
        fields = ('book', 'reader', 'comment')


class BookForm(forms.ModelForm):  
    ISBN = forms.CharField(label='ISBN',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите ISBN'}))
    title = forms.CharField(label='Наименование книги',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите Наименование книги'}))
    description = forms.CharField(label='Описание книги',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите Описание книги'}))
    year_release = forms.IntegerField(label='Год рождения',
                           widget=forms.NumberInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите Год издания'}))
    author = forms.ModelChoiceField(label='Автор', queryset=Author.objects.all(),
                                     widget=forms.Select(
                                         attrs={'class': 'form-control',
                                                'placeholder': 'Автор'}))
    copy_count = forms.IntegerField(label='Количество копий',
                           widget=forms.NumberInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите Количество копий'}))
    ost_count = forms.IntegerField(label='Остаток копий',
                           widget=forms.NumberInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите Остаток копий'}))
    price = forms.DecimalField(label='Цена',
                           widget=forms.NumberInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите Цена'}))
    pubhouse = forms.ModelChoiceField(label='Издательство', queryset=PubHouse.objects.all(),
                                     widget=forms.Select(
                                         attrs={'class': 'form-control',
                                                'placeholder': 'Издательство'}))

    class Meta:  
        model = Book  
        fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'copy_count', 'ost_count','price', 'pubhouse')
