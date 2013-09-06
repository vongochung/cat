from django.db import models

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


    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = u'e_Product'


