from django.db import models

from auth_.models import User


class BookJournalBase(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True
        ordering = ('created_at',)

class Book(BookJournalBase):
    num_pages = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=15)

class Journal(BookJournalBase):
    TYPES = (
        ('BULLET', 'Bullet'),('Food', 'Food'),('Travel', 'Travel'),('Sport', 'Sport')
    )
    type = models.CharField(max_length=300, choices= TYPES)
    publisher = models.CharField(max_length=20)