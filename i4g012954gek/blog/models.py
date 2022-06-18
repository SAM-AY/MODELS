from django.db import models

# Create your models here.
from django.db import models
class Post (models. Models):
    title = models.CharField(max_length=200)
    text= models.TextField
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    created_date = models.DateTimeField('date created')
    published_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.title