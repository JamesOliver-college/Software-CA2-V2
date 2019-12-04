from django.db import models
from django.urls import reverse

class Article(models.Model):
    id = models.CharField(max_length=200, db_index=True, primary_key=True)
    headline = models.CharField(max_length=200, default='headline')
    image = models.ImageField(upload_to='images/',
                              blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('articles:article',
                        args=[self.id])
