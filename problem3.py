from rl_qlearning import Q_learning
import matplotlib.pyplot as plt
import gym

# main
if __name__ == '__main__':
    # initialize the environment
    env = gym.make('CartPole-v1')
    rl_qlearning = Q_learning(env)
    rl_qlearning.episode = 500
    rl_qlearning.simulate()
    # plot the figuire
    y = rl_qlearning.reward_history

    n = 50
    ys = [0]*len(y)
    # calculate the last 50 rewards each episode
    for i in range(len(y)):
        if i >= n:
            ys[i] = sum(y[i-n:i])/n
        else:
            ys[i] = sum(y[:i+1])/(i+1)

    ys = ys[50:]
    x = range(len(ys))
    plt.plot(x, ys)
    plt.xlabel('Episode')
    plt.ylabel('Sum of Rewards in Episode')
    # save the figure
    plt.savefig('graph/convergence 500.png')
