from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),

    # Default App
    (r'', include('home.urls')),

    # Default App
    (r'card/', include('card.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
