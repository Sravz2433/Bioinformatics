def hidden_path_probability(path, states, transition_matrix):
    # Number of states
    num_states = len(states)
    
    # Create a state index mapping
    state_idx = {state: i for i, state in enumerate(states)}
    
    # Initial probability: 1 divided by the number of states (assuming equal start probability)
    prob = 1.0 / num_states
    
    # Multiply the transition probabilities along the path
    for i in range(1, len(path)):
        from_state = path[i - 1]
        to_state = path[i]
        from_idx = state_idx[from_state]
        to_idx = state_idx[to_state]
        
        # Multiply by the transition probability from the current state to the next
        prob *= transition_matrix[from_idx][to_idx]
    
    return prob

# Example usage
path = "ABBBBBBABBBBAAAABBBABBBAAABABBAAABBBABABBBBBBBBBBA"
states = ["A", "B"]
transition_matrix = [
    [0.516, 0.484],  # Transitions from state A
    [0.1, 0.9]   # Transitions from state B
]

result = hidden_path_probability(path, states, transition_matrix)
print(f"Probability of the hidden path: {result}")
