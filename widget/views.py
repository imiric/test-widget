# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def widget(request):
    return render(request, 'widget.html')
