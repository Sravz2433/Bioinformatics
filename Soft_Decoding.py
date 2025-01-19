import numpy as np

def forward(x, states, start_prob, trans_prob, emit_prob):
    n_states = len(states)
    T = len(x)
    forward_matrix = np.zeros((T, n_states))
    
    # Initialization step
    for i in range(n_states):
        forward_matrix[0][i] = start_prob[i] * emit_prob[i][x[0]]
    
    # Recursion step
    for t in range(1, T):
        for j in range(n_states):
            forward_matrix[t][j] = sum(forward_matrix[t-1][i] * trans_prob[i][j] for i in range(n_states)) * emit_prob[j][x[t]]
    
    return forward_matrix

def backward(x, states, trans_prob, emit_prob):
    n_states = len(states)
    T = len(x)
    backward_matrix = np.zeros((T, n_states))
    
    # Initialization step
    backward_matrix[T-1] = np.ones(n_states)
    
    # Recursion step
    for t in range(T-2, -1, -1):
        for i in range(n_states):
            backward_matrix[t][i] = sum(backward_matrix[t+1][j] * trans_prob[i][j] * emit_prob[j][x[t+1]] for j in range(n_states))
    
    return backward_matrix

def soft_decoding(x, states, start_prob, trans_prob, emit_prob):
    x = [alphabet.index(c) for c in x]  # Map symbols to indices
    forward_matrix = forward(x, states, start_prob, trans_prob, emit_prob)
    backward_matrix = backward(x, states, trans_prob, emit_prob)
    
    T = len(x)
    n_states = len(states)
    
    posterior_matrix = np.zeros((T, n_states))
    
    # Compute posterior probabilities
    for t in range(T):
        denom = sum(forward_matrix[t][j] * backward_matrix[t][j] for j in range(n_states))
        for i in range(n_states):
            posterior_matrix[t][i] = (forward_matrix[t][i] * backward_matrix[t][i]) / denom
    
    return posterior_matrix

# Input for the given example
x = "xyzzxxzzzy"
alphabet = ['x', 'y', 'z']
states = ['A', 'B']
start_prob = [0.5, 0.5]  # Assuming equal starting probabilities for both states
trans_prob = [[0.521,	0.479],  # Transition from A to A/B
              [0.488,	0.512]]  # Transition from B to A/B
emit_prob = [[0.258,	0.448,	0.294],  # A emits x, y, z
             [0.347,	0.275,	0.378]]  # B emits x, y, z

# Compute the soft decoding matrix
posterior_matrix = soft_decoding(x, states, start_prob, trans_prob, emit_prob)

# Output the result in the required format
print("A\tB")
for row in posterior_matrix:
    print(f"{row[0]:.4f}\t{row[1]:.4f}")
