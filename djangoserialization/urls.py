from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dserialization/', include('dserialization.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'customserialization.views.index'),
    (r'^default1/$', 'customserialization.views.default1'),
    (r'^default2/$', 'customserialization.views.default2'),
    (r'^custom1/$', 'customserialization.views.custom1'),
    (r'^custom2/$', 'customserialization.views.custom2')
)
