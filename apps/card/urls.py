from django.conf.urls import *
from card.views import *

urlpatterns = patterns('card.views',
   url(r'^$', 'index'),
   url(r'shopping_card', 'my_shopping_card'),
   url(r'remove', 'remove_product')

)
