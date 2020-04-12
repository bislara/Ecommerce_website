from django.http import Http404
from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404


from .models import Product

class ProductFeaturedView(ListView):
    template_name = "products/list.htm"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured_list.htm"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.htm"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.htm"

    def get_context_data(self, *args, **kwargs):
        print(args)
        print(kwargs)
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)  # get_by_id is the custom function to get the value
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

    # we can also do the above using pre-defined function filter
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.htm", context)

   
def product_detail_view(request, pk=None, *args, **kwargs):
    #instance = Product.objects.get(pk=pk) #id
    # instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh?")


    #instance = Product.objects.get(pk=pk) #id
    #instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh?")

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    #print(instance)


    # qs  = Product.objects.filter(id=pk)
    #print(qs)
    # if qs.exists() and qs.count() == 1: # len(qs)
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

    context = {
        'object': instance
    }
    return render(request, "products/detail.htm", context)