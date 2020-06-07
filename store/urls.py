from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('detail/<pk>', views.product_detail, name='prod_detail'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    #path('b', views.b, name="b"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="update_item")

]

