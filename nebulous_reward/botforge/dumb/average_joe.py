from nebulous_reward.botforge.base import Agent
from nebulous_reward.botforge.base import Policy
from nebulous_reward.botforge.base import Algorithm
from random import random, choice


class AJPolicy(Policy):
    def __init__(self, n_actions, epsilon):
        super().__init__(
            parameters=dict(zip(
                range(n_actions), [[]] * n_actions  # initially the average reward for each action is 0
            ))
        )

        self.choices = range(n_actions)
        self.epsilon = epsilon
        self.average_reward = dict(zip(self.choices, [0.0] * n_actions))

    def select_action(self, state):
        """
        The average joe's policy is to blindly select the next action based on the max average reward for actions
        as they are recorded each time an action is taken (via the update policy function)
        :param state: in this implementation,this function is unused
        :return: returns the action to be taken
        """
        if random() < self.epsilon:
            return max(self.average_reward, key=lambda x: self.average_reward[x])
        else:
            return choice(self.choices)

    def update_policy(self, reward, action):
        self.parameters[action].append(reward)
        self.average_reward[action] = sum(self.parameters[action]) / len(self.parameters[action])
        return None


class AJAgent(Agent):
    def __init__(self, policy, value_function):
        super().__init__(policy, value_function)

    def get_action(self, state):
        return self.policy(state)

    def learn(self, reward, action):
        return self.policy.update_policy(reward, action)


class AverageJoe(Algorithm):
    def __init__(self, agent, env):
        super().__init__(agent, env)

    def apply(self, epochs, steps):
        for epoch in range(epochs):
            observation, info = self.env.reset()

            for step in range(steps):
                action = self.agent.get_action(observation)
                observation, reward, terminated, truncated, info = self.env.step(action)

                self.agent.learn(reward, action)

                if terminated or truncated:
                    break
