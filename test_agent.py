from agents.q_learning import QLearningAgent
from env.pricing_env import PricingEnvironment

env = PricingEnvironment()

agent = QLearningAgent()

state, _ = env.reset()

action = agent.choose_action(state, env.action_space)

print("Current State :", state)
print("Selected Action :", action)

next_state, reward, done, _, _ = env.step(action)

print("Next State :", next_state)
print("Reward :", reward)

agent.update_q_table(
    state,
    action,
    reward,
    next_state
)

print("\nQ-Table\n")
print(agent.q_table)