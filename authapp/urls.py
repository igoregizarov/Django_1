from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
    path('verify/<email>/<activations_key>/', authapp.verify, name='verify')
]
