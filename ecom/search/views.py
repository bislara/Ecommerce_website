from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product
# Create your views here.

class ProductSearchView(ListView):
    template_name = "search/view.htm"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductSearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        print(query)
        if query == "":
            return Product.objects.all() 
        elif query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.all()

