from datetime import datetime, timedelta
from django.shortcuts import render_to_response, redirect, HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.conf import settings
from common.functions import get_current_user
from product.models import Product
from card.process import Card
from home.forms import OrderForm

def index(request):
    return render_to_response("home/index.html", {}, context_instance=RequestContext(request))


def list_product(request, product_type):

    if product_type == "cat":
        product_type = 1
    else:
        product_type = 2
    products = Product.objects.filter(product_type = product_type)
    return render_to_response("home/kitten.html", {'products' : products}, context_instance=RequestContext(request))



def view_card(request):

    card = Card(request)
    products = card.shopping_card

    data = []
    for product in products:
        pd = Product.objects.get(pk = int(product["product_id"]))
        data.append({"id" : pd.id, "image" : pd.image.url, 'name' : pd.name, 'price' : pd.price1, 'num' : product["num"], 'amount' : pd.price1 * int(product["num"])})
    return render_to_response("card/card.html", {'items' : data}, context_instance=RequestContext(request))


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

def checkout(request):
    if request.method == "GET":
        f = OrderForm()
        return render_to_response("home/checkout.html", {'form' : f}, context_instance=RequestContext(request))

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            products = request.session["shopping_card"]
            strPro = ""
            for product in products:
                strPro += "product_id: " + str(product["product_id"]) + " => num :" + str(product["num"])

            f = form.save(commit=False)
            f.note += strPro
            f.save()
            del request.session["shopping_card"]
            return render_to_response('home/_success.html', context_instance=RequestContext(request))
        else:

            return render_to_response('home/checkout.html', {'form': form},
                                      context_instance=RequestContext(request))