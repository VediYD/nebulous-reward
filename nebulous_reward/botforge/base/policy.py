class Policy:
    def __init__(self, parameters):
        self.parameters = parameters

    def __call__(self, state, *args, **kwargs):
        return self.select_action(state)

    def select_action(self, state):
        pass

    def update_policy(self):
        pass
