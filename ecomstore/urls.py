from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    # category
    path('category/', views.category, name = 'category'),
    path('category/savecategory', views.savecategory, name = 'savecategory'),
    path('category/edit/<int:ccode>', views.editcategory, name='editcategory'),
    path('category/delete/<int:ccode>', views.deletecategory, name='deletecategory'),
    # products
    path('products/', views.product, name='products'),
    path('products/add', views.addProduct, name='addproduct'),
    path('products/edit/<int:prodId>', views.editProduct, name = 'editproduct' ),
    path('products/delete/<int:prodId>', views.deleteProduct, name = 'deleteproduct'),
    # authentication
    path('accounts/login/', views.loginview, name = "login"),
    path('accounts/signup/', views.signup, name = "signup"),
    path('logout', views.logout_view, name = 'logout'),
    path('reset',views.passwordreset, name='reset'),
    # path('passwordreset',views.resetPassword),

]