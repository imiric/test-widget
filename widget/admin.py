# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Tag, Content

admin.site.register(Tag)
admin.site.register(Content)
