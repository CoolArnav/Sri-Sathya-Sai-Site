from django.db import models


class SortFilter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="Sort Filter Desciption")

    def __str__(self):
         return self.name


class Song(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    sort_filter = models.ForeignKey(SortFilter, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='Songs', max_length=10000)

    def __str__(self):
         return self.name

