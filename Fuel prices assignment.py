current_price_diesel_str = input("What is the current price for diesel?")
current_price_euro95_str = input("What is the current price for euro 95?")

current_price_diesel_float = float(current_price_diesel_str)
current_price_euro95_float = float(current_price_euro95_str)

tax_diesel = 180
tax_euro95 = 100

difference_tax = tax_diesel - tax_euro95
difference_fuelprice = current_price_euro95_float - current_price_diesel_float

break_even_point_km = difference_tax/difference_fuelprice
print("You need to drive at least:")
print(break_even_point_km)
print("kilometers per month to be indifferent between diesel or euro95 fuel")
