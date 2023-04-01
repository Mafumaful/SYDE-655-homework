import gym
import random

# Create the environment
env = gym.make('CartPole-v1')
env.reset()
env.render()
print(env.observation_space)

# Create the number of episodes
episodes = 10

# Loop through the episodes
for episode in range(1, episodes+1):
    # Reset the environment
    state = env.reset()
    done = False
    score = 0
    n_state = []
    action = 0

    # Loop through the environment
    while not done:
        # adjust action to make the model stable, make full use of the observation space
        n_state, reward, done, info, _ = env.step(action)
        env.render()
        if n_state[2] > 0:
            action = 1
        else:
            action = 0
        state = n_state
        score += reward
    print('Episode:{} Score:{}'.format(episode, score))
env.close()
