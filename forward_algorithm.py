def forward_algorithm(x, alphabet, states, transition_matrix, emission_matrix):
    # Create mappings from alphabet and states to indices
    char_idx = {char: i for i, char in enumerate(alphabet)}
    state_idx = {state: i for i, state in enumerate(states)}
    
    n = len(x)  # Length of the string
    m = len(states)  # Number of states
    
    # Initialize the forward table
    forward_table = [[0.0 for _ in range(m)] for _ in range(n)]
    
    # Initialization step: probability of starting in each state and emitting x[0]
    for k in range(m):
        forward_table[0][k] = (1 / m) * emission_matrix[k][char_idx[x[0]]]  # Assuming equal start probability
    
    # Recursion step: fill the forward table
    for i in range(1, n):
        for k in range(m):
            forward_prob = 0
            for l in range(m):
                forward_prob += forward_table[i-1][l] * transition_matrix[l][k]
            forward_table[i][k] = forward_prob * emission_matrix[k][char_idx[x[i]]]
    
    # Termination step: sum over the probabilities of all states at the last position
    total_prob = sum(forward_table[-1][k] for k in range(m))
    
    return total_prob

# Example usage
x = "xxxzyxzzyxzzzzzyyzyzyyxyyyyxzyzzyzxzxzyyzzzxxxxxyzzzzxxzxzxyzyzxxxyxzyyzzyyxxzzzyxzxyyzyxzxzzzyzyxzz"
alphabet = ["x", "y", "z"]
states = ["A", "B","C"]
transition_matrix = [
    [0.421,	0.191,	0.388],  # Transitions from state A
    [0.097,	0.86,	0.043],
    [0.326,	0.621,	0.053]# Transitions from state B
]
emission_matrix = [
    [0.402,	0.27,	0.328],  # Transitions from state A
    [0.269,	0.205,	0.526],
    [0.458,	0.037,	0.505]   # Emissions from state B (for x, y, z)
]

result = forward_algorithm(x, alphabet, states, transition_matrix, emission_matrix)
print(f"Probability of the outcome: {result}")
