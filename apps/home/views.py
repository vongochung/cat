from datetime import datetime, timedelta
from django.shortcuts import render_to_response, redirect, HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.conf import settings
from common.functions import get_current_user
from product.models import Product

def index(request):
    return render_to_response("home/index.html", {}, context_instance=RequestContext(request))


def list_product(request, product_type):

    if product_type == "cat":
        products = Product.objects.all()
        return render_to_response("home/kitten.html", {'products' : products}, context_instance=RequestContext(request))
    return render_to_response("home/topping.html", {}, context_instance=RequestContext(request))


def view_card(request):
    return render_to_response("home/card.html", {}, context_instance=RequestContext(request))


def set_lang(request, lang_code):
    from django import http
    from django.utils.translation import check_for_language

    response = http.HttpResponseRedirect('/')
    if not check_for_language(lang_code):
        lang_code = "en"

    if hasattr(request, 'session'):
        request.session['django_language'] = lang_code
    else:
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)

    current_player = get_current_user(request)
    if current_player is not None:
        current_player.language_code = lang_code
        current_player.save()

    return response