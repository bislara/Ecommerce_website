import random
import os
from django.db import models
import uuid
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import unique_slug_generator


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

class ProductQuerySet(models.query.QuerySet):

    def featured(self):
        return self.filter(featured=True)


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def featured(self):
        return self.get_queryset().filter(featured = True)

    # def all(self):
    #     # return self.get_queryset().filter(slug_field = slug)
    #     return self.get_queryset()
    def get_by_slug(self, slug_field):
        qs = self.get_queryset().filter(slug_field=slug_field) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=120)
# adding the slugfield to be found in URL..dont intialize unique = True, after u create a unique slug generator use that
    slug_field      = models.SlugField(null = True,blank = True,unique = True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=10.99)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured        = models.BooleanField(default = False)
    timestamp       = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def get_absolute_url(self):
        # return "/products/{slug}".format(slug=self.slug_field)
        return reverse("products:detail", kwargs={"slug_field": self.slug_field})


# python 3 
    def __str__(self):
        return self.title
# python 2
    def __unicode__(self):
        return self.title
# to get a by default slug when creating the object
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug_field:
        instance.slug_field = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product) 