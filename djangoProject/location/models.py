import uuid

from django.db import models


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fsq_id = models.UUIDField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'locations'

    def __str__(self):
        return self
