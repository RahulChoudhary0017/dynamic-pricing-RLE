import gymnasium as gym
from gymnasium import spaces
import numpy as np

from utils.demand import customer_demand, PRICE_MAP


class PricingEnvironment(gym.Env):
    """
    Custom Gymnasium Environment
    for Dynamic Pricing with Season Awareness
    """

    def __init__(self):
        super().__init__()

        # -----------------------------
        # Initial Settings
        # -----------------------------
        self.max_inventory = 100
        self.max_days = 30

        self.inventory = self.max_inventory
        self.days_left = self.max_days

        self.competitor_price = 3000

        # Booking Season
        self.season = "Normal"
        self.season_id = 1

        # -----------------------------
        # Action Space
        # -----------------------------
        # 0 = 1000
        # 1 = 2000
        # 2 = 3000
        # 3 = 4000
        # 4 = 5000
        self.action_space = spaces.Discrete(5)

        # -----------------------------
        # Observation Space
        # -----------------------------
        # State:
        # [Inventory, Days Left, Competitor Price, Season]
        #
        # Season:
        # 0 = Low
        # 1 = Normal
        # 2 = High

        self.observation_space = spaces.Box(
            low=np.array([0, 0, 2500, 0]),
            high=np.array([100, 30, 4500, 2]),
            dtype=np.int32
        )

    # =====================================================
    # RESET
    # =====================================================

    def reset(self, seed=None, options=None):
        """
        Reset Environment
        """

        super().reset(seed=seed)

        # Reset inventory and time
        self.inventory = self.max_inventory
        self.days_left = self.max_days

        # Random competitor price
        self.competitor_price = np.random.randint(2500, 4501)

        # -----------------------------
        # Select Booking Season
        # -----------------------------

        import random

        self.season = random.choice([
            "Low",
            "Normal",
            "High"
        ])

        # Convert season into numeric ID
        season_map = {
            "Low": 0,
            "Normal": 1,
            "High": 2
        }

        self.season_id = season_map[self.season]

        # -----------------------------
        # Initial State
        # -----------------------------

        state = np.array(
            [
                self.inventory,
                self.days_left,
                self.competitor_price,
                self.season_id
            ],
            dtype=np.int32
        )

        return state, {}

    # =====================================================
    # STEP
    # =====================================================

    def step(self, action):

        # -----------------------------
        # Selected Price
        # -----------------------------

        price = PRICE_MAP[action]

        # -----------------------------
        # Competitor Price Changes
        # -----------------------------

        self.competitor_price += np.random.randint(-100, 101)

        # Keep competitor price between 2500 and 4500
        self.competitor_price = int(
            np.clip(
                self.competitor_price,
                2500,
                4500
            )
        )

        # -----------------------------
        # Customer Demand
        # -----------------------------

        sold_rooms = customer_demand(
            action,
            self.days_left,
            self.competitor_price,
            self.season
        )

        # Cannot sell more rooms than available
        sold_rooms = min(
            sold_rooms,
            self.inventory
        )

        # -----------------------------
        # Update Inventory
        # -----------------------------

        self.inventory -= sold_rooms

        # -----------------------------
        # Revenue
        # -----------------------------

        revenue = sold_rooms * price

        reward = revenue

        # -----------------------------
        # Competitor Pricing Effect
        # -----------------------------

        if price > self.competitor_price:

            reward -= 2000

        else:

            reward += 1000

        # -----------------------------
        # Price Advantage Reward
        # -----------------------------

        if price < self.competitor_price:

            reward += 3000

        elif price == self.competitor_price:

            reward += 1500

        else:

            reward -= 2000

        # -----------------------------
        # Reward Engineering
        # -----------------------------

        # Bonus if all inventory is sold
        if self.inventory == 0:

            reward += 3000

        # Penalty if inventory remains near season end
        if self.days_left == 1 and self.inventory > 0:

            reward -= self.inventory * 500

        else:

            # Bonus when inventory becomes low
            if self.inventory < 20:

                reward += 2000

        # -----------------------------
        # High Price Penalty
        # -----------------------------

        if action == 4 and sold_rooms <= 2:

            reward -= 1000

        # -----------------------------
        # Inventory Pressure Reward
        # -----------------------------

        # Reserved for future optimization

        # -----------------------------
        # Move to Next Day
        # -----------------------------

        self.days_left -= 1

        # -----------------------------
        # Episode Completion
        # -----------------------------

        done = False

        if self.inventory == 0 or self.days_left == 0:

            done = True

        # -----------------------------
        # Current State
        # -----------------------------

        state = np.array(
            [
                self.inventory,
                self.days_left,
                self.competitor_price,
                self.season_id
            ],
            dtype=np.int32
        )

        return state, reward, done, False, {}

    # =====================================================
    # RENDER
    # =====================================================

    def render(self):

        print("-------------------------")
        print(f"Inventory : {self.inventory}")
        print(f"Days Left : {self.days_left}")
        print(f"Season    : {self.season}")
        print(f"Competitor Price : {self.competitor_price}")
        print("-------------------------")