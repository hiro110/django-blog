from django.db import models

# Create your models here.
from datetime import datetime

class blogdata(models.Model):
    title = models.CharField(max_length=512)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)