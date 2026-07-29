import random

# Price Levels
PRICE_MAP = {
    0: 1000,
    1: 2000,
    2: 3000,
    3: 4000,
    4: 5000
}

def customer_demand(price_level, days_left):

    # Base demand according to price
    if price_level == 0:
        demand = 15
    elif price_level == 1:
        demand = 12
    elif price_level == 2:
        demand = 10
    elif price_level == 3:
        demand = 7
    else:
        demand = 4

    # ----------------------------
    # Peak Season
    # ----------------------------
    if 10 <= days_left <= 20:
        demand += 5

    # ----------------------------
    # Weekend Rush
    # Every 7th day
    # ----------------------------
    if days_left % 7 == 0:
        demand += 3

    # ----------------------------
    # Last Minute Booking
    # ----------------------------
    if days_left <= 5:
        demand += random.randint(3, 7)

    # ----------------------------
    # Early Booking
    # ----------------------------
    elif days_left >= 20:
        demand += random.randint(-2, 2)

    # ----------------------------
    # Normal Days
    # ----------------------------
    else:
        demand += random.randint(-1, 3)

    return max(0, demand)