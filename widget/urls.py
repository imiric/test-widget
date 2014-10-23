from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^widget/', 'widget.views.widget', name='widget'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # Serve media files during development
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
