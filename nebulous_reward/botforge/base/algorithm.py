class Algorithm:
    def __init__(self, agent, env):
        self.agent = agent
        self.env = env
        self.render_history = {
            'epoch': [],
            'step': [],
            'render': []
        }

    def apply(self, epochs, steps):
        # learning method that needs to use the agent and env objects to run the training
        pass

    def _update_render_history(self, epoch, step, render):
        self.render_history['epoch'].append(epoch)
        self.render_history['step'].append(step)
        self.render_history['render'].append(render)

