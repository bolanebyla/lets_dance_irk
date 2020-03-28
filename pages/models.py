from django.db import models


class Videos(models.Model):
    url = models.TextField()
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
