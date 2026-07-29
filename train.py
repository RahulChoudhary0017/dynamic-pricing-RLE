from env.pricing_env import PricingEnvironment 
from agents.q_learning import QLearningAgent

import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

env = PricingEnvironment()


agent = QLearningAgent()

episodes = 5000

reward_history = []

for episode in range(episodes):

    state, _ = env.reset()

    done = False

    total_reward = 0

    while not done:

        action = agent.choose_action(state, env.action_space)

        next_state, reward, done, _, _ = env.step(action)

        agent.update_q_table(
            state,
            action,
            reward,
            next_state
        )

        state = next_state

        total_reward += reward

    reward_history.append(total_reward)

    agent.decay_epsilon()

    if (episode + 1) % 100 == 0:

        print(
            f"Episode {episode+1}/{episodes} | "
            f"Reward = {total_reward} | "
            f"Epsilon = {agent.epsilon:.3f}"
        )

os.makedirs("outputs", exist_ok=True)

with open("outputs/q_table.pkl", "wb") as file:
    pickle.dump(agent.q_table, file) 
    
plt.figure(figsize=(10,5))
plt.plot(reward_history)
plt.title("Training Reward")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.grid(True)

plt.savefig("outputs/reward_curve.png")
# Moving Average Reward Graph

window = 50

moving_average = []

for i in range(len(reward_history)):
    start = max(0, i - window + 1)
    moving_average.append(
        np.mean(reward_history[start:i + 1])
    )

plt.figure(figsize=(10,5))
plt.plot(moving_average, color="red")
plt.title("Moving Average Reward")
plt.xlabel("Episode")
plt.ylabel("Average Reward")
plt.grid(True)

plt.savefig("outputs/moving_average.png")

plt.show()
# Save Training Summary

with open("outputs/training_summary.txt", "w") as file:

    file.write("Training Summary\n")
    file.write("=========================\n\n")

    file.write(f"Episodes : {episodes}\n")
    file.write(f"Highest Reward : {max(reward_history)}\n")
    file.write(f"Lowest Reward : {min(reward_history)}\n")
    file.write(f"Average Reward : {sum(reward_history)/len(reward_history):.2f}\n")
    file.write(f"Final Epsilon : {agent.epsilon:.3f}\n") 
print("Training Summary Saved")
print("\nTraining Completed Successfully!")
print("Q-Table Saved")
print("Reward Graph Saved")