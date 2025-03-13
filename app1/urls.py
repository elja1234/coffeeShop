from django.urls import path
from . import views 
from .views import save_contact  # Import the save_contact function

urlpatterns = [
    path('', views.index, name='index'),  # Home page ('index.html')
    path('about/', views.about, name='about'),  # 'about.html'
    path('menu/', views.menu, name='menu'),  # 'menu.html'
    path('blog/', views.blog, name='blog'),  # 'blog.html'
    path('contact/', views.contact, name='contact'),  # 'contact.html'
    path('order/', views.order, name='order'), 
    path('product/<str:name>/', views.productDetail, name='product_detail'),  # Correct view reference for dynamic product pages.
    path('category/<str:category_name>/', views.productCategory, name='product_category'),
    path('save-contact/', save_contact, name='save_contact'),
]
