current_price_diesel_str = input("What is the current price for diesel?")
current_price_euro95_str = input("What is the current price for euro 95?")

road_tax_diesel_str = input("What is the amount of road tax for diesel per month?")
road_tax_euro95_str = input("What is the amount of road tax for euro95 per month?")

current_price_diesel_float = float(current_price_diesel_str)
current_price_euro95_float = float(current_price_euro95_str)

road_tax_diesel_float = float(road_tax_diesel_str)
road_tax_euro95_float = float(road_tax_euro95_str)

difference_tax = road_tax_diesel_float - road_tax_euro95_float
difference_fuelprice = current_price_euro95_float - current_price_diesel_float

break_even_point_km = difference_tax/difference_fuelprice
print("You need to drive")
print(break_even_point_km)
print("kilometers or more (per month) for diesel to be cheaper in comparison to euro95")
