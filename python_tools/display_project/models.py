from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=300)
    summary = models.CharField(max_length=1000)
    pypi_url = models.CharField(max_length=400)
    current_version = models.CharField(max_length=100)
    downloads_count = models.IntegerField()
