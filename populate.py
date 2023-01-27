import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carValue.settings")

import django

django.setup()
import time
from avg_price_calculator.models import Car

lines = []
objs = []
field_names = []

with open("data_reduced1.txt", "r") as f:
    lines = lines + [line.strip() for line in f]
    field_names = lines[0].split("|")
    lines = lines[1:]

f.close()
   

with open("data_reduced2.txt", "r") as f:
    lines = lines + [line.strip() for line in f]

f.close()


with open("data_reduced3.txt", "r") as f:
    lines = lines + [line.strip() for line in f]

f.close()



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

