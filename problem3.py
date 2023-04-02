from rl_qlearning import Q_learning
import matplotlib.pyplot as plt
import gym

# main
if __name__ == '__main__':
    # initialize the environment
    env = gym.make('CartPole-v1')
    rl_qlearning = Q_learning(env)
    rl_qlearning.simulate()
    # plot the figuire
    y = rl_qlearning.reward_history

    n = 50
    # calculate the average reward per 50 episodes
    y = [sum(y[i:i+n])/n for i in range(0, len(y), n)]
    x = range(len(y))
    x = [i*n for i in x]
    plt.plot(x, y)
    plt.xlabel('Episode')
    plt.ylabel('Sum of Rewards in Episode')
    # save the figure
    plt.savefig('graph/convergence 500.png')
