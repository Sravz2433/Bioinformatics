from collections import defaultdict

def estimate_hmm_parameters(x, alphabet, pi, states):
    # Step 1: Initialize the transition and emission matrices with counts
    transition_counts = defaultdict(lambda: defaultdict(int))
    emission_counts = defaultdict(lambda: defaultdict(int))
    
    # Step 2: Count transitions in the path pi
    for i in range(len(pi) - 1):
        current_state = pi[i]
        next_state = pi[i + 1]
        transition_counts[current_state][next_state] += 1
    
    # Step 3: Count emissions in the emitted string x
    for i in range(len(x)):
        state = pi[i]
        symbol = x[i]
        emission_counts[state][symbol] += 1
    
    # Step 4: Normalize the transition matrix
    transition_matrix = defaultdict(lambda: defaultdict(float))
    for state in states:
        total_transitions = sum(transition_counts[state].values())
        if total_transitions > 0:
            for next_state in states:
                transition_matrix[state][next_state] = transition_counts[state][next_state] / total_transitions
    
    # Step 5: Normalize the emission matrix
    emission_matrix = defaultdict(lambda: defaultdict(float))
    for state in states:
        total_emissions = sum(emission_counts[state].values())
        if total_emissions > 0:
            for symbol in alphabet:
                emission_matrix[state][symbol] = emission_counts[state][symbol] / total_emissions
    
    # Step 6: Print the transition matrix
    print("\t" + "\t".join(states))
    for state in states:
        print(state, end="\t")
        for next_state in states:
            print(f"{transition_matrix[state][next_state]:.3f}", end="\t")
        print()
    
    print("--------")
    
    # Step 7: Print the emission matrix
    print("\t" + "\t".join(alphabet))
    for state in states:
        print(state, end="\t")
        for symbol in alphabet:
            print(f"{emission_matrix[state][symbol]:.3f}", end="\t")
        print()

# Example usage:
x = "xxxzxzyxyxyyxxzyyyzzxxzzyxxyxxzyxyyyzyxxxyxyxyxxxzxyyyzyxzxzxyyzyyyzxzzyyzyzyxxzxyyyxzzzyyxzxzxzyxyy"
alphabet = ['x', 'y', 'z']
pi = "BBAACBBCCBAABCAAABBBACCCBBBAAABBBCCAABCACABCCBCAACAAACCCCACCCCACCCBCAAAABBAABCAABBBCAACAACBCBBCBBBBB"
states = ['A', 'B', 'C']

estimate_hmm_parameters(x, alphabet, pi, states)
