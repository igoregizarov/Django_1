import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.conf import settings
import datetime
import os
import json

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

from django.conf import settings
from django.core.cache import cache

from django.views.decorators.cache import cache_page


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_orederd_by_price():
    if settings.LOW_CACHE:
        key = 'products_orederd_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True,category__is_active=True).order_by('price')


def get_products_in_category_orederd_by_price(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_orederd_by_price_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')



#!!!

def get_hot_products():
    products = get_products()
    #products_list = Product.objects.all()
    return random.sample(list(products), 1)[0]
    #return random.sample(list(products_list), 1)[0]


def get_same_products(hot_product):
    return Product.objects.filter(category__pk=hot_product.category.pk).exclude(pk=hot_product.pk)[:3]


def main(request):
    title = 'Главная'

    # products = Product.objects.all()[:4]
    # products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:4]
    products = get_products()[:4]
    content = {
        'title': title,
        'products': products,
    }
    return render(request, 'mainapp/index.html', content)


@cache_page(3600)
def products(request, pk=None, page=1):
    title = 'продукты'
    hot_product = get_hot_products()
    # links_menu = ProductCategory.objects.filter(is_active=True)
    # same_products = Product.objects.all()
    links_menu = get_links_menu()
    same_products = get_same_products(hot_product)

    if pk is not None:
        if pk == 0:
            product_list = Product.objects.filter(is_active=True)
            category = {'name': 'все', 'pk': 0}

            paginator = Paginator(product_list, 2)
            try:
                product_paginator = paginator.page(page)
            except PageNotAnInteger:
                product_paginator = paginator.page(1)
            except EmptyPage:
                product_paginator = paginator.page(paginator.num_pages)

            content = {
                'title': 'все',
                'links_menu': links_menu,
                'products': product_paginator,
                'category': category,
                'hot_product': hot_product,
                'same_products': same_products
            }

            return render(request, 'mainapp/products_list.html', content)
        else:
            # category = ProductCategory.objects.get(pk=pk)
            category = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category__pk=pk)
            # product_list = Product.objects.filter(category__pk=category.pk)

        paginator = Paginator(product_list, 2)
        try:
            product_paginator = paginator.page(page)
        except PageNotAnInteger:
            product_paginator = paginator.page(1)
        except EmptyPage:
            product_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': category,
            'links_menu': links_menu,
            'products': product_paginator,
            'category': category,
            'hot_product': hot_product,
            'same_products': same_products
        }

        return render(request, 'mainapp/products_list.html', content)

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'продукты'
    links_menu = get_links_menu()
    product = get_product(pk)

    content = {
        'title': title,
        #'links_menu': ProductCategory.objects.filter(is_active=True),
        #'product': get_object_or_404(Product, pk=pk),
        'links_menu': links_menu,
        'product': product,
    }

    return render(request, 'mainapp/product.html', content)


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
        'locations': locations,
    }
    return render(request, 'mainapp/contacts.html', content)


#
# def products_all(request):
#     link_menu = [
#         {'href': 'products_all', 'name': 'все'},
#         {'href': 'products_home', 'name': 'дом'},
#         {'href': 'products_office', 'name': 'офис'},
#         {'href': 'products_modern', 'name': 'модерн'},
#         {'href': 'products_classic', 'name': 'классика'},
#     ]
#
#     content = {
#         'title': 'Продукты',
#         'link_menu': link_menu
#     }
#     return render(request, 'mainapp/products.html', content)
#
#
# def products_home(request):
#     link_menu = [
#         {'href': 'products_all', 'name': 'все'},
#         {'href': 'products_home', 'name': 'дом'},
#         {'href': 'products_office', 'name': 'офис'},
#         {'href': 'products_modern', 'name': 'модерн'},
#         {'href': 'products_classic', 'name': 'классика'},
#     ]
#
#     content = {
#         'title': 'Продукты',
#         'link_menu': link_menu
#     }
#     return render(request, 'mainapp/products.html', content)
#
#
# def products_office(request):
#     link_menu = [
#         {'href': 'products_all', 'name': 'все'},
#         {'href': 'products_home', 'name': 'дом'},
#         {'href': 'products_office', 'name': 'офис'},
#         {'href': 'products_modern', 'name': 'модерн'},
#         {'href': 'products_classic', 'name': 'классика'},
#     ]
#
#     content = {
#         'title': 'Продукты',
#         'link_menu': link_menu
#     }
#     return render(request, 'mainapp/products.html', content)
#
#
# def products_modern(request):
#     link_menu = [
#         {'href': 'products_all', 'name': 'все'},
#         {'href': 'products_home', 'name': 'дом'},
#         {'href': 'products_office', 'name': 'офис'},
#         {'href': 'products_modern', 'name': 'модерн'},
#         {'href': 'products_classic', 'name': 'классика'},
#     ]
#
#     content = {
#         'title': 'Продукты',
#         'link_menu': link_menu
#     }
#     return render(request, 'mainapp/products.html', content)
#
#
# def products_classic(request):
#     link_menu = [
#         {'href': 'products_all', 'name': 'все'},
#         {'href': 'products_home', 'name': 'дом'},
#         {'href': 'products_office', 'name': 'офис'},
#         {'href': 'products_modern', 'name': 'модерн'},
#         {'href': 'products_classic', 'name': 'классика'},
#     ]
#
#     content = {
#         'title': 'Продукты',
#         'link_menu': link_menu
#     }
#     return render(request, 'mainapp/products.html', content)


def not_found(request, exception):
    return render(request, '404.html', status=404)
