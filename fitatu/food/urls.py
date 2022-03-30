from django.urls import path
from . import views


urlpatterns = [
    # path("", views.ListDishes.as_view(), name="dishes"),
    path("update/<str:pk>/", views.UpdateDish.as_view(), name="detail-dish"),
    path("calories/<int:_pk>/", views.CalculateDishCalories, name="calories"),
    path("", views.ListDishes.as_view(), name="dishes"),
    path("add/", views.CreateDish.as_view(), name="dish_add"),
]
