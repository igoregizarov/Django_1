from django.shortcuts import render


def main(request):
    content = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):

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


def contacts(request):

    content = {
        'title': 'Контакты',
        
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