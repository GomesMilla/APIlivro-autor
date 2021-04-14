from django.contrib import admin
from django.urls import path, include
from books.api import ViewSets as BooksViewSet
from books.api import ViewSets as AuthorViewSet
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from books.views import * 

route = routers.DefaultRouter()
route.register(r'books', BooksViewSet.BooksViewSet, basename= "Books") 
route.register(r'author', AuthorViewSet.AuthorViewSet, basename= "Author")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('list-books/',list_books, name="list_books"),
    path('list-author/',list_author, name="list_author"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
