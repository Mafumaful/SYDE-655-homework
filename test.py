import gym
import random

env = gym.make('CartPole-v1', render_mode="human")
env.reset()
env.render()
print(env.observation_space)

episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = random.choice([0, 1])
        n_state, reward, done, info, _ = env.step(action)
        print(env.step(action))
        score += reward

# close the window
env.close()
