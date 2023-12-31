from nebulous_reward.botforge.base import Agent
from nebulous_reward.botforge.base import Policy
from nebulous_reward.botforge.base import Algorithm
from nebulous_reward.util import StatusWindow
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
        self.status_window = StatusWindow()

    def apply(self, epochs, steps):
        render_mode = self.env.render_mode
        _ = self.env.reset()
        if render_mode is not None:
            _render = self.env.render()
            if render_mode != 'human':
                self._update_render_history(0, 0, _render)
            else:
                self.status_window.initialize()
                self.status_window.update(0, 0, 'NA', 'NA')

        for epoch in range(epochs):
            observation, info = self.env.reset()

            for step in range(steps):
                action = self.agent.get_action(observation)
                observation, reward, terminated, truncated, info = self.env.step(action)

                self.agent.learn(reward, action)

                if render_mode is not None:
                    if render_mode != 'human':
                        self._update_render_history(epoch, step, self.env.render())
                    else:
                        self.status_window.update(epoch, step, action, reward)

                if terminated or truncated:
                    break

        if render_mode == 'human':
            self.status_window.close()
        return None
