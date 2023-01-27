from django.db import models

# Create your models here.


class Car(models.Model):
    vin = models.CharField(max_length=100)
    year = models.IntegerField()
    make = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    trim = models.CharField(max_length=100, null=True, blank=True)
    dealer_name = models.CharField(max_length=100, null=True, blank=True)
    dealer_street = models.CharField(max_length=100, null=True, blank=True)
    dealer_city = models.CharField(max_length=100, null=True, blank=True)
    dealer_state = models.CharField(max_length=100, null=True, blank=True)
    dealer_zip = models.CharField(max_length=100, null=True, blank=True)
    listing_price = models.IntegerField(null=True, blank=True, default=0)
    listing_mileage = models.IntegerField(null=True, blank=True)
    used = models.BooleanField(null=True, blank=True)
    certified = models.BooleanField(null=True, blank=True)
    style = models.CharField(max_length=100, null=True, blank=True)
    driven_wheels = models.CharField(max_length=100, null=True, blank=True)
    engine = models.CharField(max_length=100, null=True, blank=True)
    fuel_type = models.CharField(max_length=100, null=True, blank=True)
    exterior_color = models.CharField(max_length=100, null=True, blank=True)
    interior_color = models.CharField(max_length=100, null=True, blank=True)
    seller_website = models.URLField(null=True, blank=True)
    first_seen_date = models.DateField(null=True, blank=True)
    last_seen_date = models.DateField(null=True, blank=True)
    dealer_vdp_last_seen_date = models.DateField(null=True, blank=True)
    listing_status = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.vin}"
