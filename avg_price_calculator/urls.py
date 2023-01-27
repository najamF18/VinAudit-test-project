from django.urls import path, include
from .views import CalculatePrice


urlpatterns = [
    path("calculate-price/", CalculatePrice.as_view(), name="calculate_price"),
]
