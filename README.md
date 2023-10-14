# nebulous-reward
This repo intends to have a collection of solutions for environments defined in python's gym library using reinforcement learning.

# RL Book

Sutton, R. S., & Barto, A. G. (2020). Reinforcement Learning: An Introduction second edition. The MIT Press.

http://www.incompleteideas.net/book/RLbook2020.pdf

## Concepts
Note: The information in this section has been taken from the book mentioned above. All credit goes to the original 
authors.


Reinforcement learning is learning what to do—how to map situations to actions — to maximize a numerical reward signal.
The learner is not told which actions to take, but instead must discover which actions yield the most reward by trying 
them.

1. **policy**: A policy defines the learning agent’s way of behaving at a given time. In some cases the policy may be a
simple function or lookup table, whereas in others it may involve extensive computation such as a search process. 
In general, policies may be stochastic, specifying probabilities for each action.
2. **reward**: A reward signal defines the goal of a reinforcement learning problem. The agent’s sole objective is to 
maximize the total reward it receives over the long run. The reward signal is the primary basis for altering the policy;
if an action selected by the policy is followed by low reward, then the policy may be changed to select some other 
action in that situation in the future.
3. **value function**: specifies what is good in the long run, the value of a state is the total amount of reward an 
agent can expect to accumulate over the future, starting from that state. a state might always yield a low immediate 
reward but still have a high value because it is regularly followed by other states that yield high rewards. Or the 
reverse could be true.
4. **model**: mimics the behavior of the environment, or more generally, that allows inferences to be made about how the
environment will behave. given a state and action, the model might predict the resultant next state and next reward used
for planning, by which we mean any way of deciding on a course of action by considering possible future situations 
before they are actually experienced.

## Solution Methods
This section organizes the algorithms provided in the book. This is done to mimic the books organization of algorithms 
when deciding how to structure the code files. For example, gradient bandit algorithm is provided under tabular solution
so the code that implements gradient bandit method will be given under 
`/nebulous_reward/botforge/tabular/gradient_bandit.py` and so on.

### Dumb Methods
The first addition to this repository is a dumb bot that simply selects an action based on the average reward associated
with that action. `/nebulous_reward/botforge/dumb/average_joe.py`. It simply selects the action based on epsilon greedy over
action value function based on average reward for taking an action, regardless of everything else.

