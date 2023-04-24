from django.db import models

# Create your models here.


class ArtPiece(models.Model):
    name = models.CharField(max_length=255)
    date_finished = models.DateTimeField()
