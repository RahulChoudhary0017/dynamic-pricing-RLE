import numpy as np
import random


class QLearningAgent:
    """
    Q-Learning Agent for Dynamic Pricing
    """

    def __init__(self):

        # Learning Parameters
        self.learning_rate = 0.1
        self.discount_factor = 0.95

        # Exploration Parameters
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.min_epsilon = 0.01

        # Q-Table
        self.q_table = {}

    # =====================================================
    # CHOOSE ACTION
    # =====================================================

    def choose_action(self, state, action_space):
        """
        Choose Action using Epsilon-Greedy Policy
        """

        state = tuple(state)

        # Initialize state if not present
        if state not in self.q_table:
            self.q_table[state] = np.zeros(action_space.n)

        # Exploration
        if random.uniform(0, 1) < self.epsilon:
            return action_space.sample()

        # Exploitation
        return int(np.argmax(self.q_table[state]))

    # =====================================================
    # UPDATE Q-TABLE
    # =====================================================

    def update_q_table(
        self,
        state,
        action,
        reward,
        next_state,
        done=False
    ):
        """
        Update Q-Table using Q-Learning algorithm.
        """

        state = tuple(state)
        next_state = tuple(next_state)

        # Initialize current state
        if state not in self.q_table:
            self.q_table[state] = np.zeros(5)

        # Initialize next state
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(5)

        # Current Q-value
        old_value = self.q_table[state][action]

        # Terminal state has no future reward
        if done:

            next_max = 0

        else:

            next_max = np.max(
                self.q_table[next_state]
            )

        # Q-Learning Formula
        new_value = old_value + self.learning_rate * (
            reward
            + self.discount_factor * next_max
            - old_value
        )

        # Update Q-value
        self.q_table[state][action] = new_value

    # =====================================================
    # EPSILON DECAY
    # =====================================================

    def decay_epsilon(self):
        """
        Reduce Exploration Rate
        """

        if self.epsilon > self.min_epsilon:

            self.epsilon *= self.epsilon_decay

            if self.epsilon < self.min_epsilon:

                self.epsilon = self.min_epsilon