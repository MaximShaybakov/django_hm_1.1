from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'no')
    if sort == 'no':
        phones = Phone.objects.all()
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('price').reverse()
    elif sort == 'name':
        phones = Phone.objects.all().order_by('name')

    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.get(slug=slug)
    context = {'phone': phones}
    return render(request, template, context)
