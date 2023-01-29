import os

import django

from avg_price_calculator.models import Car


def parse_value(value):
    if value == "":
        return None
    if value == "TRUE":
        return True
    if value == "FALSE":
        return False
    return value


def process_lines(lines, field_names):
    objs = []
    for line in lines:
        new_dict = dict(zip(field_names, map(parse_value, line.split("|"))))
        objs.append(Car(**new_dict))
    return objs


def bulk_create_cars(objs):
    try:
        Car.objects.bulk_create(objs)
    except Exception as e:
        print("error: ", e)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carValue.settings")
    django.setup()

    try:
        with open("data_reduced1.txt", "r") as f:
            lines = [line.strip() for line in f if line.strip()]
            field_names = lines[0].split("|")
            lines = lines[1:]
    except FileNotFoundError:
        print("File data_reduced1.txt not found.")
    except Exception as e:
        print("Error reading file:", e)
    else:
        objs = process_lines(lines, field_names)
        bulk_create_cars(objs)
