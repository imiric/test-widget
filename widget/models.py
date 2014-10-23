# -*- coding: utf-8 -*-
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Content(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    tags  = models.ManyToManyField('Tag', null=True, blank=True)
    # Other relevant fields here ...

    def __str__(self):
        return self.description
