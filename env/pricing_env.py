import gymnasium as gym
from gymnasium import spaces
import numpy as np

from utils.demand import customer_demand, PRICE_MAP

class PricingEnvironment(gym.Env):
    """
    Custom Gymnasium Environment
    for Dynamic Pricing
    """

    def __init__(self):
        super().__init__()

        # Initial Settings
        self.max_inventory = 100
        self.max_days = 30

        self.inventory = self.max_inventory
        self.days_left = self.max_days

        # Action Space (5 Price Levels)
        self.action_space = spaces.Discrete(5)

        # Observation Space
        # State = [Remaining Inventory, Days Left]
        self.observation_space = spaces.Box(
            low=np.array([0, 0]),
            high=np.array([100, 30]),
            dtype=np.int32
        )

    def reset(self, seed=None, options=None):
        """
        Reset Environment
        """
        super().reset(seed=seed)

        self.inventory = self.max_inventory
        self.days_left = self.max_days

        state = np.array(
            [self.inventory, self.days_left],
            dtype=np.int32
        )

        return state, {}

    def step(self, action):

        price = PRICE_MAP[action]

        sold_rooms = customer_demand(action, self.days_left)

        sold_rooms = min(sold_rooms, self.inventory)

        self.inventory -= sold_rooms

        reward = sold_rooms * price

        self.days_left -= 1

        done = False

        if self.inventory == 0 or self.days_left == 0:
         done = True

        state = np.array(
        [self.inventory, self.days_left],
        dtype=np.int32
       )

        return state, reward, done, False, {}

    def render(self):

        print("-------------------------")
        print(f"Inventory : {self.inventory}")
        print(f"Days Left : {self.days_left}")
        print("-------------------------")