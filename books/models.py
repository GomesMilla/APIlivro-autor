from django.db import models
from uuid import uuid4

def upload_image_book(instance, filename):
    return f"{instance.id_book}-{filename}"

def upload_image_author(instance, filename):
    return f"{instance.name}-{filename}"

class Author(models.Model):
    name = models.CharField("Nome:", max_length=60, blank=False, null=False)
    birthday = models.DateField("Data de nascimento:", blank=False, null=False)
    genero = models.CharField("Genero da escrita:", max_length=20, blank=False, null=False)
    city = models.CharField("Cidade de nascimento:", max_length=90, blank=False, null=False)
    about = models.TextField("Sobre o autor:", max_length=500, blank= False, null=False)
    lives = models.CharField("Cidade onde vive:", max_length=60, blank=False, null=False)
    image = models.ImageField(upload_to=upload_image_author,blank=True, null=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField("Título:", max_length=194)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)    
    release_year = models.IntegerField("Ano lançamento:")
    state = models.CharField("Estado do livro:", max_length=10)
    pages = models.IntegerField("Número de paginas:")
    publishing = models.CharField("Editora:", max_length=194)
    creat_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_book,blank=True, null=True)

    def __str__(self):
        return self.title