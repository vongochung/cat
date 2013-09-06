from django.conf.urls import *
from home.views import *

urlpatterns = patterns('home.views',
   url(r'^$', 'index'),
   url(r'^card/$', 'view_card'),
   url(r'^set_lang/(?P<lang_code>\w+)', 'set_lang', name='set_lang'),
   url(r'^(?P<product_type>\w+).html', 'list_product', name='product'),


)
