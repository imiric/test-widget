from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^widget/', 'widget.views.widget', name='widget'),

    url(r'^admin/', include(admin.site.urls)),
)
