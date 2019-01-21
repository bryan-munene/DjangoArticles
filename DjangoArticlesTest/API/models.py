from django.db import models

class Articles(models.Model):
    """This class represent the Articles model."""

    name = models.CharField(max_length=255, blank=False, unique=True)
    text = models.TextField(blank=False)
    author = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns human readable representation of the model instance"""
        return "{} authored by {}".format(self.text, self.name)