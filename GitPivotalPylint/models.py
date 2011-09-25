from django.contrib import admin
from django.db import models

class BaseModel(models.Model):
"""

"""
    POSITION = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
    )

    name = models.CharField(max_length=20)
    position = models.IntegerField(choices=POSITION)


admin.site.register(BaseModel)