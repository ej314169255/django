from django.utils import timezone

from django.db import models

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=5)
    image = models.ImageField(upload_to="product")
    release_date = models.TextField()
    lte_exists = models.TextField()
    slug = models.TextField()

    def __str__(self):
        return self.name