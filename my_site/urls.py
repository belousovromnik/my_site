"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from p_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.home),

    path('book/', views.book_list, name='book_list'),
    # path('book/create', views.BookCreate.as_view(), name='book_create'),  
    path('book/update/<int:pk>/', views.BookEdit.as_view(), name='book_update'),
    # path('book/delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),

    path('pubhouse/', views.pubhouse_list, name='pubhouse'),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('index/book_increment_ost/', views.book_increment_ost),
    path('index/book_decrement_ost/', views.book_decrement_ost),
    
    path('bookreader/', views.bookreader_list, name='bookreader'),
    path('bookreader/create/', views.BookreaderCreate.as_view(), name='bookreader_create'),
    path('bookreader/update/<int:pk>/', views.BookreaderEdit.as_view(), name='bookreader_update'),
    # path('bookreader/delete/<int:pk>/', ReaderDelete.as_view(), name='bookreader_delete'),

    path('author/', include(('p_library.urls', 'p_library'))),
    path('reader/', include(('reader.urls', 'reader'))),

]
