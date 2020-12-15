from django.shortcuts import render, get_object_or_404
from django.conf import settings
import datetime
import os
import json

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def main(request):
    title = 'Главная'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    products = Product.objects.all()[:4]
    content = {
        'title': title,
        'products': products,
        'basket': basket
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()


    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            product_list = Product.objects.all()
            category = {'name': 'все', 'pk': 0}

            content = {
                'title': 'все',
                'links_menu': links_menu,
                'products': product_list,
                'category': category,
                'basket': basket,
            }

            return render(request, 'mainapp/products_list.html', content)
        else:
            # category = ProductCategory.objects.get(pk=pk)
            category = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category__pk=pk)
            # product_list = Product.objects.filter(category__pk=category.pk)

        content = {
            'title': category,
            'links_menu': links_menu,
            'products': product_list,
            'category': category,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    # same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', content)


def contacts(request):

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    title = 'Контакты'
    visit_date = datetime.datetime.now()
    locations = []
    file_path = os.path.join(settings.BASE_DIR, 'contacts.json')
    with open(file_path) as file_contact:
        locations = json.load(file_contact)
    content = {
        'title': title,
        'visit_date': visit_date,
        'locations': locations,
        'basket': basket
    }
    return render(request, 'mainapp/contacts.html', content)


def products_all(request):
    link_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    content = {
        'title': 'Продукты',
        'link_menu': link_menu
    }
    return render(request, 'mainapp/products.html', content)


def products_home(request):
    link_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    content = {
        'title': 'Продукты',
        'link_menu': link_menu
    }
    return render(request, 'mainapp/products.html', content)


def products_office(request):
    link_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    content = {
        'title': 'Продукты',
        'link_menu': link_menu
    }
    return render(request, 'mainapp/products.html', content)


def products_modern(request):
    link_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    content = {
        'title': 'Продукты',
        'link_menu': link_menu
    }
    return render(request, 'mainapp/products.html', content)


def products_classic(request):
    link_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    content = {
        'title': 'Продукты',
        'link_menu': link_menu
    }
    return render(request, 'mainapp/products.html', content)
