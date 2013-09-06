from django.shortcuts import render_to_response, redirect, HttpResponse
from django.template import RequestContext
from card.process import Card
import pprint

def index(request, product_id, size):
    #Check if user logging
    card = Card(request)
    card.add(product_id, 1, size)
    return render_to_response('card/card.html',
                              {'card': card.shopping_card}, context_instance=RequestContext(request))

def my_shopping_card(request):
    card = Card(request)
    return render_to_response('card/card.html',
                              {'card': card.shopping_card}, context_instance=RequestContext(request))


def remove_product(request):

    card = Card(request)
    card.remove(1)
    return render_to_response('card/card.html',
                              {'card': card.shopping_card}, context_instance=RequestContext(request))