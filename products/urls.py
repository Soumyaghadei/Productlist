from django.urls import path
from .views import ProductListView
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register_view, name='register'),  
    path('products/', ProductListView.as_view(), name='product-list'),
    
]



