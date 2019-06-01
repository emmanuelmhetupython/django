from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,default='Emmanuel')
    pdf   = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers', null=True,blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=10)
    post = models.TextField(max_length=20)

    def __str__(self):
        return self.post



