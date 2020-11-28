from django.shortcuts import render
from django.conf import settings
import datetime
import os
import json
from mainapp.models import Product, ProductCategory


def main(request):
    title = 'Главная'
    products = Product.objects.all()[:4]
    content = {
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)
    link_menu = ProductCategory.objects.all()
    # link_menu = [
    #     {'href': 'products_all', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    # ]

    content = {
        'title': 'Продукты',
        'link_menu': link_menu
    }
    return render(request, 'mainapp/products.html', content)


def contacts(request):
    title = 'Контакты'
    visit_date = datetime.datetime.now()
    locations = []
    file_path = os.path.join(settings.BASE_DIR, 'contacts.json')
    with open(file_path) as file_contact:
        locations = json.load(file_contact)
    content = {
        'title': title,
        'visit_date': visit_date,
        'locations': locations
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
