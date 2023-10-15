class Agent:
    def __init__(self, policy, value_function):
        self.policy = policy
        self.value = value_function

    def get_action(self, state):
        pass

    def learn(self, reward, action):
        pass
