from django.db import models

# Create your models here.

class Benih(models.Model):
    jumlah_beras = models.PositiveIntegerField()
    jumlah_jagung = models.PositiveIntegerField()
    jumlah_kacang = models.PositiveIntegerField()