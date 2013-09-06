from django.db import models
from django.conf import settings
import datetime
class Category(models.Model):
    name = models.CharField(max_length=250)
    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = u"e_Category"

class Product(models.Model):
    name  = models.CharField(max_length=250)
    product_type  = models.ForeignKey(Category)
    price1 = models.IntegerField()
    price2 = models.IntegerField()
    price3 = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to= "upload")

    def image_tag(self):

        return u'<img src="%s" width="100px" height="100px"/>' % ("/" + self.image.url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = u'e_Product'


class Order(models.Model):
    name  = models.CharField(max_length=300)
    phone = models.IntegerField()
    email = models.EmailField()
    order_date = models.DateTimeField(default = datetime.datetime.now())
    orders_note = models.CharField(max_length=1000)
    note = models.CharField(max_length=300)
    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = u"e_Order"