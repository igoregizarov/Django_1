from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser

from mainapp.models import ProductCategory, Product

# users


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()
    content = {
        'update_form': user_form
    }
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    users_list = ShopUser.objects.all().order_by('-is_active')
    content = {
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {
        'update_form': edit_form
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    user_item = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        if user_item.is_active:
            user_item.is_active = False
        else:
            user_item.is_active = True
        user_item.save()
        return HttpResponseRedirect(reverse('admin:users'))
    content = {
        'user_to_delete': user_item
    }
    return render(request, 'adminapp/user_delete.html', content)

# categories


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        category_form = ProductCategoryEditForm()
    content = {
        'update_form': category_form
    }
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    categories_list = ProductCategory.objects.all().order_by('-is_active')
    content = {
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    edit_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:category_update', args=[edit_category.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    content = {
        'update_form': edit_form
    }
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    category_item = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        if category_item.is_active:
            category_item.is_active = False
        else:
            category_item.is_active = True
        category_item.save()
        return HttpResponseRedirect(reverse('admin:categories'))
    content = {
        'category_to_delete': category_item
    }
    return render(request, 'adminapp/category_delete.html', content)

# products


def product_create(request, pk):
    pass


def products(request, pk):
    category_item = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category=category_item)
    content = {
        'objects': products_list,
        'category': category_item
    }

    return render(request, 'adminapp/products.html', content)


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass