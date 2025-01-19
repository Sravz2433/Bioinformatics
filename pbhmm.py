def profile_hmm():
    # Step 1: Input parsing
    theta = 0.278
    alphabet = ['A', 'B', 'C', 'D', 'E']
    alignment = [
        "BE--BAEAB",
"BEDABAE-B",
"-DAAB-EAB",
"B-AA--EAB",
"B-AABAAEA"
    ]
    
    num_sequences = len(alignment)
    alignment_len = len(alignment[0])
    
    # Step 2: Identify match states based on threshold
    match_cols = []
    gap_threshold = theta * num_sequences
    
    for col in range(alignment_len):
        gap_count = sum(1 for row in alignment if row[col] == '-')
        if gap_count <= gap_threshold:
            match_cols.append(True)  # Match column
        else:
            match_cols.append(False)  # Insert column
    
    num_match_states = sum(match_cols)
    
    # Step 3: Initialize the transition and emission matrices
    states = []
    for i in range(num_match_states):
        states.append('M' + str(i))  # Match states: M0, M1, ...
        states.append('I' + str(i))  # Insert states: I0, I1, ...
        states.append('D' + str(i))  # Delete states: D0, D1, ...
    states.append('S')  # Start state
    states.append('E')  # End state
    
    transition_matrix = {state: {state: 0 for state in states} for state in states}
    emission_matrix = {state: {symbol: 0 for symbol in alphabet} for state in states if state.startswith('M') or state.startswith('I')}
    
    # Step 4: Populate transition and emission matrices
    for seq in alignment:
        seq_state = ['S']  # Start at S
        
        match_state_idx = 0
        for i in range(alignment_len):
            if match_cols[i]:
                if seq[i] == '-':
                    seq_state.append('D' + str(match_state_idx))  # Add delete state
                else:
                    seq_state.append('M' + str(match_state_idx))  # Add match state
                    emission_matrix['M' + str(match_state_idx)][seq[i]] += 1
                    match_state_idx += 1  # Increment match state index when there's a match
            else:
                if seq[i] != '-':
                    if match_state_idx > 0:  # Ensure valid index for insert state
                        seq_state.append('I' + str(match_state_idx - 1))  # Add insert state
                        emission_matrix['I' + str(match_state_idx - 1)][seq[i]] += 1
        
        seq_state.append('E')  # End at E
        
        # Count transitions
        for s1, s2 in zip(seq_state[:-1], seq_state[1:]):
            transition_matrix[s1][s2] += 1
    
    # Step 5: Normalize transition and emission matrices
    for state in transition_matrix:
        total_transitions = sum(transition_matrix[state].values())
        if total_transitions > 0:
            for next_state in transition_matrix[state]:
                transition_matrix[state][next_state] /= total_transitions
    
    for state in emission_matrix:
        total_emissions = sum(emission_matrix[state].values())
        if total_emissions > 0:
            for symbol in emission_matrix[state]:
                emission_matrix[state][symbol] /= total_emissions
    
    # Step 6: Print matrices
    def print_matrix(matrix, label):
        print(label)
        states = list(matrix.keys())
        print("\t" + "\t".join(states))
        for state in states:
            print(state + "\t" + "\t".join(f"{matrix[state][s]:.3f}" for s in states))
    
    print_matrix(transition_matrix, "Transition Matrix:")
    
    def print_emission_matrix(matrix, alphabet):
        print("--------")
        print("\t" + "\t".join(alphabet))
        for state in matrix:
            print(state + "\t" + "\t".join(f"{matrix[state][s]:.3f}" for s in alphabet))
    
    print_emission_matrix(emission_matrix, alphabet)

# Call the function to see the output
profile_hmm()
