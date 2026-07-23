from env.pricing_env import PricingEnvironment

env = PricingEnvironment()

state, _ = env.reset()

done = False

while not done:

    action = env.action_space.sample()

    state, reward, done, _, _ = env.step(action)

    print("=" * 40)
    print("Action :", action)
    print("State  :", state)
    print("Reward :", reward)

    env.render()