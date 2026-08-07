import random

PRICE_MAP = {
    0: 1000,
    1: 2000,
    2: 3000,
    3: 4000,
    4: 5000
}

def customer_demand(action, days_left, competitor_price, season):

    our_price = PRICE_MAP[action]

    # Base demand
    if our_price < competitor_price:
        demand = random.randint(12, 16)

    elif our_price == competitor_price:
        demand = random.randint(8, 12)

    else:
        demand = random.randint(4, 8)

    # Last-minute bookings
    if days_left <= 5:
        demand += random.randint(3, 6)

    # Early booking
    elif days_left >= 20:
        demand += random.randint(-1, 2)
        
        # Season Ending Discount
    if days_left <= 3:
       demand += random.randint(2, 5) 
       
       
       # -----------------------------
       # Season Effect
       # -----------------------------
    if season == "High":
       demand += random.randint(4, 7)

    elif season == "Low":
       demand -= random.randint(2, 4)

       # Normal season -> no change

    return max(0, demand)