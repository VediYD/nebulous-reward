import sys
import os

REPO_DIR = os.path.join(os.getcwd(), 'nebulous_reward')
sys.path.append(os.path.dirname(REPO_DIR))

from nebulous_reward import AverageJoe, AJAgent, AJPolicy

import gymnasium as gym


if __name__ == '__main__':
    # initialize policy, agent, and environment
    policy = AJPolicy(4, 0.5)
    agent = AJAgent(policy, None)
    env = gym.make('FrozenLake-v1', render_mode='human')

    # setup and train algorithm
    algorithm = AverageJoe(agent, env)
    algorithm.apply(10, 20)

    print(policy.parameters)
    print(policy.average_reward)
    print(algorithm.render_history)
