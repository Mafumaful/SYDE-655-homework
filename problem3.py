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
    # calculate the average reward per 50 episodes
    y = [sum(y[i:i+50])/50 for i in range(0, len(y), 50)]
    x = range(len(y))
    x = [i*50 for i in x]
    plt.plot(x, y)
    plt.xlabel('Episode')
    plt.ylabel('Sum of Rewards in Episode')
    # save the figure
    plt.savefig('convergence.png')

    # change the epsilon
    rl_qlearning.update = False
    rl_qlearning.epsilon = 0
    rl_qlearning.reward_history = []
    rl_qlearning.simulate()
    y = rl_qlearning.reward_history

    # plot the figure
    y = [sum(y[i:i+50])/50 for i in range(0, len(y), 50)]
    x = range(len(y))
    x = [i*50 for i in x]
    plt.plot(x, y)
    plt.xlabel('Episode')
    plt.ylabel('Sum of Rewards in Episode')
    # save the figure
    plt.savefig('convergence after.png')
