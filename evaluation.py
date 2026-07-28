import random
import matplotlib.pyplot as plt

from env.pricing_env import PricingEnvironment
from agents.q_learning import QLearningAgent

# Load Environment
env = PricingEnvironment()

# Load Trained Agent
agent = QLearningAgent()
import pickle

with open("outputs/q_table.pkl", "rb") as file:
    agent.q_table = pickle.load(file)

agent.epsilon = 0

fixed_total = 0
random_total = 0
qlearning_total = 0

episodes = 100

# -------------------------
# Fixed Pricing Strategy
# -------------------------
for _ in range(episodes):

    state, _ = env.reset()
    done = False

    while not done:

        action = 2   # Fixed Price Level

        state, reward, done, _, _ = env.step(action)

        fixed_total += reward


# -------------------------
# Random Pricing Strategy
# -------------------------
for _ in range(episodes):

    state, _ = env.reset()
    done = False

    while not done:

        action = random.randint(0, env.action_space.n - 1)

        state, reward, done, _, _ = env.step(action)

        random_total += reward


# -------------------------
# Q-Learning Strategy
# -------------------------
agent.epsilon = 0

for _ in range(episodes):

    state, _ = env.reset()
    done = False

    while not done:

        action = agent.choose_action(state, env.action_space)

        state, reward, done, _, _ = env.step(action)

        qlearning_total += reward


print("\n========== RESULT ==========")

print(f"Fixed Strategy Revenue      : {fixed_total}")
print(f"Random Strategy Revenue     : {random_total}")
print(f"Q-Learning Revenue          : {qlearning_total}")

# Graph
labels = ["Fixed", "Random", "Q-Learning"]
values = [fixed_total, random_total, qlearning_total]

plt.figure(figsize=(8,5))
plt.bar(labels, values)

plt.title("Revenue Comparison")
plt.ylabel("Revenue")

plt.savefig("outputs/comparison.png")

plt.show()