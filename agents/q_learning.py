import numpy as np
import random


class QLearningAgent:
    """
    Q-Learning Agent for Dynamic Pricing
    """

    def __init__(self):

        # Learning Parameters
        self.learning_rate = 0.2
        self.discount_factor = 0.99

        self.epsilon = 1.0
        self.epsilon_decay = 0.998
        self.min_epsilon = 0.05
        # Q-Table
        self.q_table = {}

    def choose_action(self, state, action_space):
        """
        Choose Action using Epsilon-Greedy Policy
        """

        state = tuple(state)

        # Exploration
        if random.uniform(0, 1) < self.epsilon:
            return action_space.sample()

        # Initialize state if not present
        if state not in self.q_table:
            self.q_table[state] = np.zeros(action_space.n)

        # Best Action
        return np.argmax(self.q_table[state])

    def update_q_table(
        self,
        state,
        action,
        reward,
        next_state
    ):
        """
        Update Q-Table
        """

        state = tuple(state)
        next_state = tuple(next_state)

        if state not in self.q_table:
            self.q_table[state] = np.zeros(5)

        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(5)

        old_value = self.q_table[state][action]

        next_max = np.max(self.q_table[next_state])

        new_value = old_value + self.learning_rate * (
            reward +
            self.discount_factor * next_max -
            old_value
        )

        self.q_table[state][action] = new_value

    def decay_epsilon(self):
        """
        Reduce Exploration Rate
        """

        if self.epsilon > self.min_epsilon:
            self.epsilon *= self.epsilon_decay

            if self.epsilon < self.min_epsilon:
                self.epsilon = self.min_epsilon