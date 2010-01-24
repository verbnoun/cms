from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/home/79691/domains/cms.itbox.es/html/media/js/tiny_mce/' }),
    (r'^search/$', 'cms.search.views.search'),
    # catchall
    (r'', include('django.contrib.flatpages.urls')),
)
