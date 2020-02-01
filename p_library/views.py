
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.db import models

from datetime import datetime

from .models import Book, Author, PubHouse, Bookreader
from .forms import AuthorForm, BookForm, BookreaderForm

from reader.models import Reader

def home(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


def book_list(request):
    template = loader.get_template('book_list.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


class BookEdit(UpdateView):  
    model = Book  
    form_class = BookForm  
    template_name = 'book_edit.html'  
    success_url = reverse_lazy('book_list')  


def author_list(request):
    template = loader.get_template('author_list.html')
    author = Author.objects.all()
    biblio_data = {
        "objects_list": author,
    }
    return HttpResponse(template.render(biblio_data, request))

class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_create.html'
    success_url = reverse_lazy('author_list')


class AuthorEdit(UpdateView):  
    model = Author  
    form_class = AuthorForm  
    template_name = 'author_edit.html'  
    success_url = reverse_lazy('author_list')  


class AuthorDelete(DeleteView):
    model = Author
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('author_list')


def bookreader_list(request):
    template = loader.get_template('bookreader_list.html')
    bookreaders = Bookreader.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "bookreaders": bookreaders,
    }

    return HttpResponse(template.render(biblio_data, request))


class BookreaderCreate(CreateView):
    model = Bookreader
    form_class = BookreaderForm
    template_name = 'bookreader_create.html'
    success_url = reverse_lazy('bookreader')

    def form_valid(self, form):
        data = form.cleaned_data
        book_id = data['book'].id

        book_db = Book.objects.filter(id=book_id).first()
        book_db.ost_count -= 1
        book_db.save()
        print('book_db-copy_count ', book_db.copy_count)
        print('book_db-ost_count ', book_db.ost_count)
        return super().form_valid(form)


class BookreaderEdit(UpdateView):  
    model = Bookreader  
    form_class = BookreaderForm  
    template_name = 'bookreader_edit.html'  
    success_url = reverse_lazy('bookreader')  

    def form_valid(self, form):
        data = form.cleaned_data
        book_id = data['book'].id
        print('book_id')
        print(book_id)
        book_db = Book.objects.filter(id=book_id).first()
        print('book_db-copy_count ', book_db.copy_count)
        print('book_db-ost_count ', book_db.ost_count)
        return super().form_valid(form)


def author_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  #  Первым делом, получим класс, который будет создавать наши формы. Обратите внимание на параметр `extra`, в данном случае он равен двум, это значит, что на странице с несколькими формами изначально будет появляться 2 формы создания авторов.
    if request.method == 'POST':  #  Наш обработчик будет обрабатывать и GET и POST запросы. POST запрос будет содержать в себе уже заполненные данные формы
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='author')  #  Здесь мы заполняем формы формсета теми данными, которые пришли в запросе. Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм, но и разных формсетов, этот параметр позволяет их отличать в запросе.
        if author_formset.is_valid():  #  Проверяем, валидны ли данные формы
            for author_form in author_formset:  
                author_form.save()  #  Сохраним каждую форму в формсете
            return HttpResponseRedirect(reverse_lazy('author_list'))  #  После чего, переадресуем браузер на список всех авторов.
    else:  #  Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        author_formset = AuthorFormSet(prefix='author')  #  Инициализируем формсет и ниже передаём его в контекст шаблона.
    return render(request, 'manage_authors.html', {'author_formset': author_formset})


def pubhouse_list(request):
    template = loader.get_template('pubhouse_list.html')
    pubhouse = PubHouse.objects.all().order_by('name')

    cont = []
    for item in pubhouse:
        books = Book.objects.filter(pubhouse=item.id).order_by('author__full_name', 'title')
        c_inc = []
        for book in books:
            c_inc.append(book.author.full_name + ' - ' + book.title)

        pub_inc = {}
        pub_inc[item.name] = c_inc
        cont.append(pub_inc)

    biblio_data = {
        "objects_list": cont,
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book/')
            book.copy_count += 1
            book.save()
        return redirect('/book/')
    else:
        return redirect('/book/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/book/')
    else:
        return redirect('/book/')


def book_increment_ost(request):
    if request.method == 'POST':
        bookreader_id = request.POST['id']
        if not bookreader_id:
            return redirect('/bookreader/')
        else:
            bookreader = Bookreader.objects.filter(id=bookreader_id).first()
            if not bookreader or bookreader.datain is not None:
                return redirect('/bookreader/')            
            print('bookreader.datain', bookreader.datain)
            bookreader.datain = datetime.now()
            print('bookreader', bookreader.datain)
            print('bookreader.id', bookreader.book.id)
            book = Book.objects.filter(id=bookreader.book.id).first()
            if not book:
                return redirect('/bookreader/')
            book.ost_count += 1
            print('book', book.ost_count)
            bookreader.save()
            book.save()
        return redirect('/bookreader/')
    else:
        return redirect('/bookreader/')


def book_decrement_ost(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book/')
            if book.ost_count < 1:
                book.ost_count = 0
            else:
                book.ost_count -= 1
            book.save()
        return redirect('/book/')
    else:
        return redirect('/book/')
