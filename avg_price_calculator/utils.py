def calculate_avg_price(cars):
    """
    This function takes the filtered car objects and returns the calculated average price
    """
    avg_price = "N/A"
    prices = list(
        cars.exclude(listing_price=None).values_list("listing_price", flat=True)
    )
    if prices:
        avg_price = round(sum(prices) / len(cars), -2)

    return avg_price