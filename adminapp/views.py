from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser

from mainapp.models import ProductCategory, Product


# users


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#     content = {
#         'update_form': user_form
#     }
#     return render(request, 'adminapp/user_update.html', content)


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')
    fields = '__all__'
    # form_class = ShopUserAdminEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователь/создание'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     users_list = ShopUser.objects.all().order_by('-is_active')
#     content = {
#         'objects': users_list
#     }
#     return render(request, 'adminapp/users.html', content)


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    # paginate_by = 2

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователи'
        return context


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
        'form': edit_form
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


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         category_form = ProductCategoryEditForm()
#     content = {
#         'update_form': category_form
#     }
#     return render(request, 'adminapp/category_update.html', content)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    # fields = '__all__'
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/создание'
        return context


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    categories_list = ProductCategory.objects.all().order_by('-is_active')
    content = {
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:category_update', args=[edit_category.pk]))
#     else:
#         edit_form = ProductCategoryEditForm(instance=edit_category)
#
#     content = {
#         'update_form': edit_form
#     }
#     return render(request, 'adminapp/category_update.html', content)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    # fields = '__all__'
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         if category_item.is_active:
#             category_item.is_active = False
#         else:
#             category_item.is_active = True
#         category_item.save()
#         return HttpResponseRedirect(reverse('admin:categories'))
#     content = {
#         'category_to_delete': category_item
#     }
#     return render(request, 'adminapp/category_delete.html', content)


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/удаление'
        return context

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
            self.object.save()
        else:
            self.object.is_active = True
            self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# products


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'продукт/создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('adminapp:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    content = {'title': title,
               'form': product_form,
               'category': category
               }

    return render(request, 'adminapp/product_update.html', content)
# def product_create(request, pk):
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         update_form = ProductEditForm(request.POST, request.FILES)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('adminapp:products', args=[pk]))
#     else:
#         update_form = ProductEditForm()
#
#     content = {
#         'form': update_form,
#         'category': category_item
#     }
#
#     return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    category_item = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category=category_item)
    content = {
        'objects': products_list,
        'category': category_item,
    }

    return render(request, 'adminapp/products.html', content)


# class ProductListView(ListView):
#     model = Product
#     template_name = 'adminapp/products.html'
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         category_item = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'продукты'
#         context['category'] = category_item
#         return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     pruduct_item = get_object_or_404(Product, pk=pk)
#     content = {
#         'object': pruduct_item
#     }
#     return render(request, 'adminapp/product_read.html', content)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'товар'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         update_form = ProductEditForm(request.POST, request.FILES, instance=product_item)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('adminapp:products', args=[pk]))
#     else:
#         update_form = ProductEditForm(instance=product_item)
#
#     content = {
#         'update_form': update_form,
#         'category': product_item.category
#     }
#
#     return render(request, 'adminapp/product_update.html', content)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'продукт/редактирование'
        return context

    def get_success_url(self):
        update_product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return reverse_lazy('admin:products', args=[update_product.category.pk])


# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         if product.is_active:
#             product.is_active = False
#         else:
#             product.is_active = True
#         product.save()
#         return HttpResponseRedirect(reverse('admin:products', args=[product.category_id]))
#     content = {
#         'product_to_delete': product
#     }
#     return render(request, 'adminapp/product_delete.html', content)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'продукт/удаление'
        return context

    def get_success_url(self):
        delete_product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return reverse_lazy('admin:products', args=[delete_product.category.pk])

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
            self.object.save()
        else:
            self.object.is_active = True
            self.object.save()

        return HttpResponseRedirect(self.get_success_url())