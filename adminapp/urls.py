from django.urls import path, include

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # path('users/create/', adminapp.user_create, name='user_create'),
    path('users/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    # path('users/read/', adminapp.users, name='users'),
    path('users/read/', adminapp.UsersListView.as_view(), name='users'),

    path('users/update/<pk>/', adminapp.user_update, name='user_update'),

    path('orders/read/', adminapp.OrderListView.as_view(), name='orders'),
    path('orders/update/<pk>/', adminapp.order_update, name='order_update'),

    path('users/delete/<pk>/', adminapp.user_delete, name='user_delete'),
    path('orders/delete/<pk>/', adminapp.order_delete, name='order_delete'),

    # path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/create/', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    # path('categories/update/<pk>/', adminapp.category_update, name='category_update'),
    path('categories/update/<pk>/', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    # path('categories/delete/<pk>/', adminapp.category_delete, name='category_delete'),
    path('categories/delete/<pk>/', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<pk>/', adminapp.product_create, name='product_create'),
    path('products/read/category/<pk>/', adminapp.products, name='products'),
    # path('products/read/category/<pk>/', adminapp.ProductListView.as_view(), name='products'),
    # path('products/read/<pk>/', adminapp.product_read, name='product_read'),
    path('products/read/<pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    # path('products/update/<pk>/', adminapp.product_update, name='product_update'),
    path('products/update/<pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),

    # path('products/delete/<pk>/', adminapp.product_delete, name='product_delete'),
    path('products/delete/<pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
]
