from django.db import models


class Link(models.Model):
    shortened_link = models.CharField(max_length=100, primary_key=True)
    link = models.URLField(max_length=150)

    def __str__(self) -> str:
        return self.shortened_link
