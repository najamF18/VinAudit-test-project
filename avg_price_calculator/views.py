from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Car
from django.db.models import Q

# Create your views here.


class CalculatePrice(TemplateView):

    template_name = "search.html"

    def get(self, request, *args, **kwargs):
        return render(request, "search.html")

    def post(self, request, *args, **kwargs):
        avg_price = "N/A"
        year = request.POST["yearinput"]
        model = request.POST["modelinput"]
        make = request.POST["makeinput"]
        mileage = int(request.POST["mileageinput"])
        cars = Car.objects.filter(
            Q(listing_mileage__gte=mileage + 5000)
            | Q(listing_mileage__lte=mileage - 5000),
            year=year,
            model=model,
            make=make,
        )
        prices = list(
            cars.exclude(listing_price=None).values_list("listing_price", flat=True)
        )
        if prices:
            avg_price = round(sum(prices) / len(cars), -2)
        return render(
            request,
            "results.html",
            context={"avg_price": avg_price, "cars": cars[:100]},
        )
