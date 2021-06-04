#implementing the basic gym loop for Pendulum-v0 environment
import gym

env = gym.make("Pendulum-v0")

while True:
    obs = env.reset()
    done = False
    while not done:
        # in practice the action comes from your policy
        action = env.action_space.sample()

        obs, rew, done, misc = env.step(action)
        # optional
        env.render()