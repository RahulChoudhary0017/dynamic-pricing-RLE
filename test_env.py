from env.pricing_env import PricingEnvironment

env = PricingEnvironment()

state, _ = env.reset()

print("\n========== INITIAL STATE ==========")
print("State :", state)
print("Season:", env.season)
print("===================================")

for i in range(5):

    action = env.action_space.sample()

    state, reward, done, _, _ = env.step(action)

    print("\n-----------------------------------")
    print("Day              :", i + 1)
    print("Action           :", action)
    print("State            :", state)
    print("Inventory        :", state[0])
    print("Days Left        :", state[1])
    print("Competitor Price :", state[2])
    print("Season ID        :", state[3])
    print("Season           :", env.season)
    print("Reward           :", reward)
    print("-----------------------------------")

    if done:
        break

print("\n========== TEST COMPLETED ==========")