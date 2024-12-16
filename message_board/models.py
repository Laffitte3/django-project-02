from django.db import models

# Create your models here.
class Post(models.Model):

    title=models.CharField(max_length=200)
    body=models.TextField()

    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.title