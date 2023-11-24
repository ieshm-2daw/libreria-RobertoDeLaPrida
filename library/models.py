from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    dni = models.CharField(max_length=10)
    direcction = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()

    
class Libro(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField('Author')
    editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE)
    published_date = models.DateField()

    GENRE = (
        ('N','Novel'),
        ('F','Fantasy'),
        ('T','Theatre'),
        ('O','Other'),
    )

    genre = models.CharField(max_length=1,choices=GENRE)
    isbn = models.IntegerField(max_length=13, unique=True)
    resume = models.TextField()
    front_page = models.ImageField(upload_to='front_pages/',blank=True,null=True)

    

    AVAILABILITY = (
            ('A', 'Aviable'),
            ('G', 'Given'),
        )
    
    availability = models.CharField(max_length=1, choices=AVAILABILITY)
        #portada = models.ImageField() #Neceista Pillow

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    biography = models.TextField()
    #foto = models.ImageField() #Necesita Pillow

class Editorial(models.Model):
    name = models.CharField(max_length=100, unique=True)
    direcction = models.TextField()
    website = models.URLField()

class Loan(models.Model):
    book = models.ForeignKey('Libro', on_delete=models.CASCADE)
    given_date = models.DateField()
    return_date = models.DateField()
    user = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    STATE = (
        ('G', 'Given'),
        ('R', 'Returned'),
    )
    state = models.CharField(max_length=1, choices=STATE)