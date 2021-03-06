from django.conf import settings
from django.contrib import auth
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm, ShopUserProfileEditForm
from authapp.models import ShopUser


def send_verify_email(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activations_key])

    subject = 'Подтверждение'

    message = f'{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activations_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activations_key == activations_key and not user.is_activations_key_expired():
            user.activations_key = ''
            user.is_active = True
            user.save()
            auth.login(request, user)
            # request.user.is_authenticated
        return render(request, 'authapp/verification.html')
    except Exception as e:
        print('error')


def login(request):
    title = 'вход'
    next_url = request.GET.get('next', '')
    login_form = ShopUserLoginForm(data=request.POST or None)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('main'))
    content = {'title': title, 'login_form': login_form, 'next': next_url}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'регистрация'
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_email(user):
                print('success')
            else:
                print('error')
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = ShopUserRegisterForm

    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)


# def edit(request):
#     title = 'редактирование'
#     if request.method == 'POST':
#         edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('authapp:edit'))
#     else:
#         edit_form = ShopUserEditForm(instance=request.user)
#         content = {'title': title, 'edit_form': edit_form}
#         return render(request, 'authapp/edit.html', content)


@transaction.atomic
def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(
            instance=request.user.shopuserprofile
        )

    content = {
        'title': title,
        'edit_form': edit_form,
        'profile_form': profile_form
    }

    return render(request, 'authapp/edit.html', content)