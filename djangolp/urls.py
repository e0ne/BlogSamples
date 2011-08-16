from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'dlp.views.index'),
    (r'^updates$', 'dlp.views.updates'),
    (r'^updates2$', 'dlp.views.updates2'),
)
