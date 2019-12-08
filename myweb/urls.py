from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^books/', views.book_list, name='book_list'),
    url(r'^class/books/', views.BookListView.as_view(), name='class_book_list'),
    url(r'^class/upload/', views.UploadBookView.as_view(), name='class_upload_book'),
    url(r'^books/upload/', views.upload_book, name='upload_book'),
    url(r'^books/(?P<pk>\d+)',views.delete_book,name='delete_book'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)