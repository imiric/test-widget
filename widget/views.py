# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Content

def widget(request):
    context = {
        'contents': Content.objects.filter(tags__name__in=['starting'])
    }
    return render(request, 'widget.html', context)
