from django.template import RequestContext


class Card:

    def __init__(self, request):

        if "shopping_card" not in request.session:
            request.session["shopping_card"] = []
        self.shopping_card = request.session["shopping_card"]
        self.request = request

    def add(self, product_id, num, size):

        if len(self.shopping_card) > 0:
            update = False
            for product in self.shopping_card:
                if int(product_id) == int(product["product_id"]):
                    update_product = {"product_id": product_id, "num": product["num"] + num, "size" : size}
                    self.shopping_card[self.shopping_card.index(product)] = update_product
                    update = True
                    break

            if update is False:
                self.shopping_card.append({"product_id": product_id, "num": num, "size" : size})

        else:
            self.shopping_card.append({"product_id": product_id, "num": num, "size" : size})
        self.request.session["shopping_card"] = self.shopping_card
        return self.request

    def remove(self, product_id):

        if len(self.shopping_card) >= 1:
            for product in self.shopping_card:
                if product_id == product["product_id"]:
                    self.shopping_card.remove(product)
        self.request.session["shopping_card"] = self.shopping_card
        return  self.request