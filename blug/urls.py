from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'blug.views.index'),
    (r'^(\d+)/(\d+)/(\d+)/([-_a-z0-9]+)/$', 'blug.views.entry'),
    #(r'^([-_a-z0-9]+).text/$', 'blug.views.view_source'),
)
