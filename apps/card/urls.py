from django.conf.urls import *
from card.views import *

urlpatterns = patterns('card.views',
   url(r'add/(?P<product_id>\w+)/(?P<size>\d+)$', 'index'),
   url(r'update/(?P<product_id>\w+)/(?P<num>\d+)$', 'update_product'),
   url(r'shopping_card', 'my_shopping_card'),
   url(r'remove/(?P<product_id>\d+)', 'remove_product')
)
