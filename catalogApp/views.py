from django.shortcuts import render

from catalogApp.models import Product, Contacts


def home(request):
    late_product = Product.objects.order_by('-create_date')[:5]

    for product in late_product:
        print(product.name, product.price_for_pcs)

    return render(request, 'catalogApp/home.html', {'late_product': late_product})


def contacts(request):
    contacts = Contacts.objects.all()
    return render(request, 'catalogApp/contacts.html', {'contacts': contacts})
