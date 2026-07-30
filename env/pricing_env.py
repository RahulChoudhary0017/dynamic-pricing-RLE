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
        
        self.competitor_price = 3000
         
        # Action Space (5 Price Levels)
        self.action_space = spaces.Discrete(5)

        # Observation Space
        # State = [Remaining Inventory, Days Left]
        self.observation_space = spaces.Box(
            low=np.array([0, 0, 0]),
            high=np.array([100, 30, 2]),
            dtype=np.int32
        )

    def reset(self, seed=None, options=None):
        """
        Reset Environment
        """
        super().reset(seed=seed)

        self.inventory = self.max_inventory
        self.days_left = self.max_days
        self.competitor_price = np.random.randint(2500, 4501)

        state = np.array(
            [self.inventory, self.days_left],
            dtype=np.int32
        )

        return state, {}

    def step(self, action):

     price = PRICE_MAP[action] 
       # Competitor price changes every day
     self.competitor_price += np.random.randint(-100, 101)

       # Keep competitor price in range
     self.competitor_price = int(
         np.clip(
             self.competitor_price,
             2500,
             4500
         )
     )

     # Customer Demand
     sold_rooms = customer_demand(action, self.days_left)
     sold_rooms = min(sold_rooms, self.inventory)

     # Update Inventory
     self.inventory -= sold_rooms

     # Revenue
     revenue = sold_rooms * price

     reward = revenue
     # Competitor Pricing Effect

     if price > self.competitor_price:

       reward -= 2000

     else:

      reward += 1000

     # -----------------------------
     # Reward Engineering
     # -----------------------------

     # Bonus if all inventory sold
     if self.inventory == 0:
        reward += 3000

     # Penalty if inventory remains at season end
     if self.days_left == 1 and self.inventory > 0:
        reward -= self.inventory * 500
     else:

         if self.inventory < 20:

               reward += 2000

     # Small penalty for keeping price too high
     if action == 4 and sold_rooms <= 2:
        reward -= 1000

     # Move to next day
     self.days_left -= 1

     done = False

     if self.inventory == 0 or self.days_left == 0:
        done = True

     if self.competitor_price < 2800:
        competitor_level = 0      # Low
     elif self.competitor_price < 3600:
        competitor_level = 1      # Medium
     else:
         competitor_level = 2      # High

     state = np.array(
    [
        self.inventory,
        self.days_left,
        competitor_level
    ],
    dtype=np.int32
)


     return state, reward, done, False, {}

    def render(self):

        print("-------------------------")
        print(f"Inventory : {self.inventory}")
        print(f"Days Left : {self.days_left}")
        print("-------------------------")