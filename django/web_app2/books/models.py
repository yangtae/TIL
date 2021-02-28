from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100) #책 제목
    authors = models.ManyToManyField('Author') #책 저자
    publisher = models.ForeignKey('Publisher',on_delete=CASCADE) # 책 출판사
    publication_date = models.DateField() # 책 출판일

    def __str__(self): 
        return self.title

    def __repr__(self):
        return self.tilte

class Author(models.Model):
    salutation = models.CharField(max_length=100) #저자 인사말
    name = models.CharField(max_length=50) # 저자 이름
    email = models.EmailField() # 저자 이메일

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()