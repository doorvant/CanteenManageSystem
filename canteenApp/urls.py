from django.urls import path
from canteenApp import views

urlpatterns = [
    path("", views.init),
    path("order_food1/", views.order1),
    path("order_food2/", views.order2),
    path("order_food3/", views.order3),
    path("order_list/", views.order_list),
    path("edit_score/", views.edit_score),
    path("score/", views.score),
    path("payed/", views.payed),
    path("add_food/", views.add_food),
    path("edit_food/", views.edit_food),
    path("delete_food/", views.delete_food),
    path("delete_order/", views.delete_order),
    path("food_list/", views.food_list),
    path("money/", views.money),
]
