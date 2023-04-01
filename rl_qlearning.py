import gym
import numpy as np
import random


class Q_learning:
    def __init__(self, env):
        # initialize the environment
        self.buckets = 5  # number of buckets
        self.alpha = 0.5  # learning rate
        self.gamma = 0.9  # discount factor
        self.epsilon = 0.9  # exploration rate
        self.action = 2  # number of actions
        self.env = env  # environment

        self.episode = 1000  # number of episodes

        # initialize the Q-table with random values
        self.q_table = np.random.uniform(
            size=(self.buckets, self.buckets, self.buckets, self.buckets, self.action
                  ))

        self.reward_history = []

    # discretize the state
    def discretize(self, continuous_state):
        continuous_state = [x-0.5 for x in continuous_state]
        state = [0, 0, 0, 0]
        # set up dimension states
        state[0] = np.linspace(-4.8, 4.8, self.buckets+1)[1:-1]
        state[1] = np.linspace(-3.0, 3.0, self.buckets+1)[1:-1]
        state[2] = np.linspace(-0.418, 0.418, self.buckets+1)[1:-1]
        state[3] = np.linspace(-2.0, 2.0, self.buckets+1)[1:-1]

        result = [0, 0, 0, 0]
        # discretize the state
        result[0] = np.digitize(continuous_state[0], state[0])
        result[1] = np.digitize(continuous_state[1], state[1])
        result[2] = np.digitize(continuous_state[2], state[2])
        result[3] = np.digitize(continuous_state[3], state[3])

        return tuple(result)

    # select an action based on the Q-table and the exploration rate
    def choose_action(self, state):

        if random.uniform(0, 1) < self.epsilon:
            # choose a random action
            action = np.random.choice(self.action)
        else:
            # make sure it chosed the nearest q
            d_state = self.discretize(state)
            q_value_a = \
                self.q_table[d_state[0]][d_state[1]][d_state[2]][d_state[3]]
           # choose the action with the highest Q-value
            if q_value_a[0] > q_value_a[1]:
                action = 0
            else:
                action = 1
        return action

    # simulate
    def simulate(self):
        for current_episode in range(self.episode):
            rewards = []
            state, _ = self.env.reset()
            state = list(state)
            action = self.choose_action(state)
            print("current episode {}".format(current_episode))
            end = False
            while not end:
                stateindex = self.discretize(state)  # discretize state
                action_a = self.choose_action(state)  # choose action
                statenext, reward, end, _, _ = self.env.step(
                    action_a)  # take action
                rewards.append(reward)  # add reward
                statenext = list(statenext)  # list state
                statenextindex =\
                    self.discretize(statenext)  # know the index of state
                # return the index of the maximum value
                QMaxOfNext = np.max(self.q_table[statenextindex])

                # update the Q-table
                if not end:
                    error = reward + self.gamma * QMaxOfNext -\
                        self.q_table[stateindex][action_a]
                    self.q_table[stateindex][action_a] =\
                        self.q_table[stateindex][action_a] + \
                        self.alpha * error
                else:
                    error = reward - self.q_table[stateindex][action_a]
                    self.q_table[stateindex][action_a] =\
                        self.q_table[stateindex][action_a] + \
                        self.alpha * error
                state = statenext
            print("reward {}".format(sum(rewards)))
            self.reward_history.append(sum(rewards))