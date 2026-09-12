"""
This is file containg the function calculate_delivery_cost(price)   
The function returns the delivery cost based on the price of the item
"""

def calculate_delivery_cost(price):
    if price > 50:
        return "$0.00"   
    if 20 <= price  <= 50:
        return "$3.99"
    if price < 20:
        return "$6.99"

if __name__ == "__main__":
    print(calculate_delivery_cost())