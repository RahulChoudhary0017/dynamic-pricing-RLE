import random

PRICE_MAP = {
    0: 3000,
    1: 3500,
    2: 4000,
    3: 4500,
    4: 5000
}


def customer_demand(action, days_left):
    """
    Simulate customer demand based on price and remaining days.
    """

    base_demand = {
        0: 10,
        1: 8,
        2: 6,
        3: 4,
        4: 2
    }

    demand = base_demand[action]

    # Last 5 days → demand increases
    if days_left <= 5:
        demand += 2

    # Random variation
    demand += random.randint(-2, 2)

    return max(0, demand)