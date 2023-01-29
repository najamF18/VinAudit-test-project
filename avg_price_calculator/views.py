from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Car
from django.db.models import Q
from .utils import calculate_avg_price

# Create your views here.


class CalculatePrice(TemplateView):

    template_name = "search.html"

    def get(self, request, *args, **kwargs):
        """
        Displays a web page to enter values for calculating the average price
        """
        return render(request, "search.html")

    def post(self, request, *args, **kwargs):
        """
        Filters Cars according to the values provided and returns average price
        """
        year = request.POST["yearinput"]
        model = request.POST["modelinput"]
        make = request.POST["makeinput"]
        mileage = int(request.POST["mileageinput"])
        cars = Car.objects.filter(
            Q(listing_mileage__gte=mileage + 5000)
            | Q(listing_mileage__lte=mileage - 5000),
            year=year,
            model__icontains=model,
            make__icontains=make,
        )
        avg_price = calculate_avg_price(cars)
        return render(
            request,
            "results.html",
            context={"avg_price": avg_price, "cars": cars[:100]},
        )
