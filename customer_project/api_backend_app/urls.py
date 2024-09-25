from django.urls import path
from .views import customer_list, customer_details_view, order_list, order_details_view,order_item_list,order_item_details_view

urlpatterns = [
    path('', customer_list),
    path('customer/<str:passed_name>', customer_details_view),
    path('orders', order_list),
    path('order/<int:passed_id>', order_details_view),
    path('order_items', order_item_list),
    path('order_item/<str:passed_item_name>', order_item_details_view),

]
