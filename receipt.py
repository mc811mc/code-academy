# lovely loveseats for neat suites on fleet street

lovely_loveseat_price = 254.00
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""

stylish_settee_price = 180.50
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""

luxurious_lamp_price = 52.15
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""

sales_tax = 0.088

customer_one_total = 0
customer_one_itemization = ""

customer_one_total = lovely_loveseat_price + stylish_settee_price + luxurious_lamp_price

customer_one_itemization = lovely_loveseat_description + stylish_settee_description + luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
