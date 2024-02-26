from django.urls import path

from catalogApp.views import home, contacts

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
]