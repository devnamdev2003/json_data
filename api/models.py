from django.db import models

class MyModel(models.Model):
    json_data = models.JSONField()
