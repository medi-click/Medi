from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('register/', views.registerPage , name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/',views.logoutPage, name='logout'),
    

    path('index/',views.index_view, name='index'),
    path('product_details/<str:pk>/',views.product_details_view, name='product_details'),
    
    
    path('about/',views.about_view,name = 'about'),
    path('cart/',views.cart_view, name='cart'),
    path('checkout/',views.checkout_view, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('wish_item/', views.wishItem, name='wish_item'),
    path('wishlist/',views.wishlist_view,name='wishlist'),
    path('category/<str:pk>',views.category_view,name='category'),
    path('paypal/',views.paypal,name='paypal'),
    path('search',views.search,name='search'),
    




    #path("",views.index,name="index"),
    path("register/",views.iregister,name='register'),
    path("signin/",views.isignin,name="signin"),
    path("profile/",views.iprofile,name='profile'),
    path("signout/",views.isignout,name='signout'),
    path("changepassword/",views.ichangepass,name='changepass'),
    path("newpass/",views.inewpass,name='newpass'),
    path("updateprofile/",views.iupdateprofile,name='updateprofile'),

    # path("customer/",views.customer,name='updateprofile'),
    # path("retailer/",views.retailer,name='updateprofile'),
    # path("wholesaler/",views.wholesaler,name='updateprofile'),
    path("products/",views.iproducts,name='products'),
    path("addstock/",views.iadd_stock,name='addstock'),
    path("search/",views.isearchresults,name='searchresults'),

    

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

    path('site/',views.siteView,name='site'),

    
    
]
