from django.core.management import BaseCommand

from catalogApp.models import Category, Product, Contacts


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_add = [
            {'name': 'Овощ'},
            {'name': 'Фрукт'},
            {'name': 'Ягода'},
            {'name': 'Мясо'},
        ]
        category_list = [Category(**category_item) for category_item in category_add]
        Category.objects.bulk_create(category_list)

        categoty_f = Category.objects.get(name='Фрукт')
        categoty_v = Category.objects.get(name='Овощ')

        product_add = [
            {'name': 'Яблоко', 'description': 'свежее', 'category': categoty_f, 'price_for_pcs': 28, },
            {'name': 'Банан', 'description': 'привезен из Турции', 'category': categoty_f, 'price_for_pcs': 35, },
            {'name': 'Капуста', 'description': 'выращена в деревне', 'category': categoty_v, 'price_for_pcs': 42, },
            {'name': 'Картофель', 'description': 'выращен в теплицах', 'category': categoty_v, 'price_for_pcs': 24, },
            {'name': 'Апельсин', 'description': 'выращен в теплицах', 'category': categoty_f, 'price_for_pcs': 76, },
            {'name': 'Огурец', 'description': 'выращен в теплицах', 'category': categoty_v, 'price_for_pcs': 15, },
        ]

        product_list = [Product(**product_item) for product_item in product_add]
        Product.objects.bulk_create(product_list)


