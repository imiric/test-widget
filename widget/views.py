# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Content

@xframe_options_exempt
def widget(request):
    context = {
        'contents': Content.objects.filter(tags__name__in=['starting'])
    }
    return render(request, 'widget.html', context)
