from ..base import ValueFunction
from ..base import Agent
from ..base import Policy
from ..base import Algorithm

class AverageJoe(Algorithm):
    def __init__(self, agent, env):
        super().__init__(agent, env)

    def train(self, steps):
        observation, info = self.env

        for step in range(steps):
            action = self.agent.get_action(observation)
            observation, reward, terminated, truncated, info = self.env.step(action)

            if terminated or truncated:
                observation, info = self.env.reset()

            self.agent.learn(reward)



