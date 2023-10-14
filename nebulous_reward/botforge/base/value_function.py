class ValueFunction:
    def __init__(self, parameters):
        self.parameters = parameters

    def __call__(self, state, *args, **kwargs):
        return self.get_value(state)

    def get_value(self, state):
        pass

    def update_function(self):
        pass
