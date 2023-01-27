import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carValue.settings")

import django

django.setup()
import time
from avg_price_calculator.models import Car


with open("car_data.txt", "r") as f:
    lines = [line.strip() for line in f]
    field_names = lines[0].split("|")
    lines = lines[1:]
    objs = []

    program_starts = time.time()
    for line in lines:
        new_dict = dict()
        for field, value in zip(field_names, line.split("|")):
            if value == "":
                print("null spotted")
                value = None

            if value == "TRUE":
                value = True
            if value == "FALSE":
                value = False
            new_dict[field] = value

        objs.append(Car(**new_dict))
        now = time.time()
    Car.objects.bulk_create(objs)


f.close()
