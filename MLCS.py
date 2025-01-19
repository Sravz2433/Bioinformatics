def mlcs(X, Y, Z):
    m, n, o = len(X), len(Y), len(Z)
    
    # Create a 3D DP table
    dp = [[[0] * (o + 1) for _ in range(n + 1)] for __ in range(m + 1)]
    backtrack = [[[None] * (o + 1) for _ in range(n + 1)] for __ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if X[i-1] == Y[j-1] == Z[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    backtrack[i][j][k] = (i-1, j-1, k-1)
                else:
                    choices = [(dp[i-1][j][k], (i-1, j, k)),
                               (dp[i][j-1][k], (i, j-1, k)),
                               (dp[i][j][k-1], (i, j, k-1))]
                    dp[i][j][k], backtrack[i][j][k] = max(choices, key=lambda x: x[0])
    
    # Length of the longest common subsequence
    lcs_length = dp[m][n][o]
    
    # Trace back to find the LCS and the alignment
    i, j, k = m, n, o
    alignment_X, alignment_Y, alignment_Z = [], [], []
    
    while i > 0 or j > 0 or k > 0:
        if backtrack[i][j][k] is None:
            break

        prev_i, prev_j, prev_k = backtrack[i][j][k]
        
        if i > prev_i:
            alignment_X.append(X[i-1])
        else:
            alignment_X.append('-')
        if j > prev_j:
            alignment_Y.append(Y[j-1])
        else:
            alignment_Y.append('-')
        if k > prev_k:
            alignment_Z.append(Z[k-1])
        else:
            alignment_Z.append('-')
        
        i, j, k = prev_i, prev_j, prev_k
    
    # Since we traced back, the alignment is in reverse order
    alignment_X.reverse()
    alignment_Y.reverse()
    alignment_Z.reverse()
    
    return lcs_length, ''.join(alignment_X), ''.join(alignment_Y), ''.join(alignment_Z)

# Example Input
X = "TTGTTGGG"
Y = "GAGGGGAGC"
Z = "ATCTTAAA"

# Function Call
length, align_X, align_Y, align_Z = mlcs(X, Y, Z)
print(f"Length of MLCS: {length}")
print(f"{align_X}")
print(f"{align_Y}")
print(f"{align_Z}")
