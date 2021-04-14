from rest_framework import viewsets
from books.api import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = models.Books.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title__contains=title)

        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author=author)
        return queryset
    

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AuthorSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = models.Author.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__contains=name)
        return queryset
    