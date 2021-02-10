from django.db import models

from shortener.models import PyShoURL
# Create your models here.

class ClickEventManager(models.Manager):
    def create_event(self, pyshoInstance):
        if isinstance(pyshoInstance, PyShoURL):
            obj, created = self.get_or_create(pysho_url=pyshoInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    pysho_url   = models.OneToOneField(PyShoURL, on_delete=models.CASCADE)  # associates
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
