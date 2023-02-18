from scipy import stats
from .models import Car


def calculate_avg_price(input_mileage):
    """
    This function takes the filtered car objects and returns the calculated average price
    """
    Car.objects.filter(listing_mileage=None).update(listing_mileage=0)
    Car.objects.filter(listing_price=None).update(listing_price=0)
    all_cars = Car.objects.all()
    prices = list(all_cars.values_list("listing_price", flat=True))
    mileage = list(all_cars.values_list("listing_mileage", flat=True))

    slope, intercept, r, p, std_err = stats.linregress(mileage, prices)

    avg_price = slope * input_mileage + intercept

    return avg_price
