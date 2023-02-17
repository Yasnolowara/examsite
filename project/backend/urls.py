from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html/', views.index, name='index'),
    path('categories.html/', views.categories, name='categories'),
    path('check-out.html/', views.checkout, name='check-out'),
    path('contact.html/', views.index, name='contact'),
    path('main.html/', views.index, name='main'),
    path('product-page.html/', views.index, name='product-page'),
    path('shopping-cart.html/', views.index, name='shopping-cart'),
    path('register/', views.registerPage, name='register'),

]