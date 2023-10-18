
# Pseudo code of the function

```plaintext
 Function get_state_utilities(epsilon, rewards):
    state_count = length of rewards
    utilities = list of size state_count, initialized with infinity
    discount = 1
    delta = infinity

    while (delta > epsilon) if discount == 1 else (delta * (1 - discount) / discount > epsilon):
        delta = 0
        for state in range(state_count):
            utility = rewards[state] + max(
                0.95 * (probability * utilities[next_state] for next_state in get_next_states(state, action)),
                0.025 * (probability * utilities[next_state] for next_state in get_next_states(state, sideways_actions))
            )
            delta = max(delta, abs(utility - utilities[state]))
            utilities[state] = utility

    return utilities
```

