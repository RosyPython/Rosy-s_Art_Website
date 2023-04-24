from django.db import models

# Create your models here.


class ArtPiece(models.Model):
    name = models.CharField(max_length=255)
    date_finished = models.DateField(
        (), auto_now=False, auto_now_add=False)
    image = models.CharField(
        max_length=255, default="https://i.imgur.com/nQtyN1F.png")
