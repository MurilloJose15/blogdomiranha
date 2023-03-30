from django.db import models

class Post(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado','Publicado'),
    )
    titulo = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)
    corpo = models.TextField()
    
