from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.product_list, name="products"),
    path('product/<slug:slug>/', views.product_details, name='product_details'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:pk>/', views.update_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
  ]