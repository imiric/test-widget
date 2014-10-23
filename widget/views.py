# -*- coding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_GET

from .models import Content

def widget(request):
    context = {
        'contents': Content.objects.filter(tags__name__in=['starting'])
    }
    return render(request, 'widget.html', context)

@require_GET
def images_by_tag(request, tag):
    """Return the URLs of images that match the given tag"""
    if not request.is_ajax():
        return HttpResponseBadRequest()

    prefix = 'http://{}'.format(get_current_site(request))
    data = {'status': 'OK'}

    image_urls = ['{}{}'.format(prefix, c.image.url)
            for c in Content.objects.filter(tags__name__in=[tag])]
    data.update({'data': image_urls})

    return JsonResponse(data)
