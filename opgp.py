def outcome_probability_given_path(x, alphabet, path, states, emission_matrix):
    # Create a mapping from alphabet characters to indices
    char_idx = {char: i for i, char in enumerate(alphabet)}
    
    # Create a mapping from states to indices
    state_idx = {state: i for i, state in enumerate(states)}
    
    # Initialize the probability
    prob = 1.0
    
    # Multiply the emission probabilities for each position
    for i in range(len(x)):
        char = x[i]
        state = path[i]
        char_index = char_idx[char]
        state_index = state_idx[state]
        
        # Multiply by the emission probability of x_i from state π_i
        prob *= emission_matrix[state_index][char_index]
    
    return prob

# Example usage
x = "zyzxzzzyyyxxzyxxyzxyzxzxzyxxzxxzxzyzxzyyzxxxzzxzyz"
alphabet = ["x","y","z"]
path = "AABABBAAAAABABBAABBABBBBABABABABBAAAABBBAABBBBBABB"
states = ["A", "B"]
emission_matrix = [
    [0.443,	0.263,	0.294],  # Emissions from state A (for x, y, z)
    [0.398,	0.14,	0.462]   # Emissions from state B (for x, y, z)
]

result = outcome_probability_given_path(x, alphabet, path, states, emission_matrix)
print(f"Probability of the outcome given the hidden path: {result}")
