from django.shortcuts import render


def home(request):
    return render(request, 'catalogApp/home.html')


def contacts(request):
    return render(request, 'catalogApp/contacts.html')
