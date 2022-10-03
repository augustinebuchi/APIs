from django.contrib import admin
from django.urls import path
from myapp import views
from rest_framework import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Customers/', views.Customer_list),
    path('products/', views.product_list),
    path('Products/<int:id>', views.product_detail),
    #path('order/', views.order_hist),  <coming to it>
]

urlpatterns = format_suffix_patterns(urlpatterns)
