import sys

def score(a, b, match, mismatch, indel):
    if a == b:
        return match
    elif a == '-' or b == '-':
        return -indel
    else:
        return -mismatch

def nw_score(s, t, match, mismatch, indel):
    previous = [0] * (len(t)+1)
    for j in range(1, len(t)+1):
        previous[j] = previous[j-1] - indel
    for i in range(1, len(s)+1):
        current = [0] * (len(t)+1)
        current[0] = previous[0] - indel
        for j in range(1, len(t)+1):
            match_score = previous[j-1] + (match if s[i-1]==t[j-1] else -mismatch)
            delete = previous[j] - indel
            insert = current[j-1] - indel
            current[j] = max(match_score, delete, insert)
        previous = current
    return previous

def middle_edge(s, t, match, mismatch, indel):
    n = len(s)
    m = len(t)
    mid = n // 2  # Splitting based on s (V)
    
    # Compute score_l using the first half of s and entire t
    score_l = nw_score(s[:mid], t, match, mismatch, indel)
    
    # Compute score_r using the second half of s and entire t, both reversed
    score_r = nw_score(s[mid:][::-1], t[::-1], match, mismatch, indel)
    
    max_score = float('-inf')
    split = 0
    
    # Iterate j from 0 to m to find the best split
    for j in range(len(t)+1):
        if (len(t) - j) < len(score_r):
            total = score_l[j] + score_r[len(t)-j]
            if total > max_score:
                max_score = total
                split = j
        # Else, skip to avoid IndexError
    
    # Now determine the edge
    i = mid
    j = split
    candidates = []
    if i < n and j < m:
        candidates.append(((i, j), (i+1, j+1), match if s[i]==t[j] else -mismatch))
    if i < n:
        candidates.append(((i, j), (i+1, j), -indel))
    if j < m:
        candidates.append(((i, j), (i, j+1), -indel))
    
    # Choose the best
    candidates.sort(key=lambda x: x[2], reverse=True)
    return candidates[0][0], candidates[0][1]

def main():
    # Example Parameters (Replace these with file reading if needed)
    match, mismatch, indel = 1, 1, 5
    s = ("GTGTCGTCATGTTGGTACTTTTGGGTTTCGATCTAGTACAAAAGCAGCTGCATCATACAATAAAGTACCCCGGTATAGGATAGCTCTTTAGGAGTATCAATTAAGACGGCTCATTGAACAAGGATTGGGTGGGCCGTTCGTGTAACGGGAGATCTACACTAGGAATAAACGCTGCACGGAAGGCATCTTCAGGAGATAATGCGGTGGTAGACAGCCTTATATACTTACTGGCGAGTTATAAGAACGACAGGAAGGTAAAAATGTTCGGTGAAAAGACTCCAATCACTCATACCGAATCTAGAGGTTAGCCTAGCCTACTTCGACTTCTCCACATTATGTATTCGAACTTCACTCAATGCTCAGGTAATCGCAAGCACAGTGATGGTTCCCCTTAATGTTTGCGGGACCACTTTCACGTAATGGCGGTCAAAGGTGCACCGGCTAGGTTGCGAGCAAGCGGTCTTTGAGTAGCGGGACGACCCAGGGAGAATCAATAGCGTGAAGGGGTTCAATTAGCGTGCCATCCTGCCCTATCCCATGTGTAAATGAAGGCCTCTGTCTTTTCTTAATATCTTAGCCACTCGAACGGTACCGTTCGGTAAATACAATTTTCAAATGTGCCAGTCTCTGTATCGATACCCCCCCGGGCCGACAAAAGTGTTGTAAAGAAGCGGGTTCAGGTCCTGAGTCTAATCGCAGTTCAGAAGGAACACATTTACTGTGTGAGCCGCCGCGGATTAGAGCGGACCATTACCAATCATGATGAGCCTACCGATTCAGGAGTAGTGGCGTGCCGGAGAACAAAGGGGCTTAACATGTTCTGAACCGATACCACTAAGAGTCAATCGGGCATTCCGTTCGTGACAGTTTACCGTGACGCGTAATGAGTTTCGTCCATGA")
    t = ("GTATCGCTTTTGGGTCTCGATCTAGTACAAAGCCGGATCATACGACAAAGTACCAGACAAGTCCGGAGAGCTCGTATCAATGAAGACGGGATCCCGGGTATGCACACGTGAAACGGGAGGTGGCCTCTACACTAGGCGCTGCACGGAAGTCATCGACAGGAGATAATGCGGTGGTAGAGACAGCGTTATATACTTACTGGAGAAGGATTCGACACAATTTCTAAAAATGTTCGTCGAAAAGACTCCAATCCCTCATACAGAATCTAGAGATTAGCCTAGCCTTGGTATCCACATCATGTATTCGTCACTCGATAGTCACTGGGGCAAGCATAGCAACGATGGTGCACCGGTCATATTAATTGCGGGAAACAAGGGCTCTTTCACGTAATGGCGGTCAAAGGTGCAACGTAACCGGGTATGTCAAACGGTTGAGTACTAATTTAGCGTGACTAGTTCGACCGTGACTGTAGGGAGAGAGAACGGTGTGTAGGGGTTCAGTGATAAGCGTGCCATCATGCTTTGCCCTTTCCCACGTGCAAATGAAGGCCACGCACTCTTATAATCCCCAATACCTTGGCCATTTTGCTACGAAAGGTACCGTTCGGTTGTAAAGATCGCTTTGCCATATAAATGCGAGTCACCAGTCTTTATCGATACCACCCCGGACCGATGAAAAGTGTTGTAAAGTGCATTAGCGTTCGCAGAGGTCCTGAGTCTAATCGCAGCGAAGAAACATATTTACTGGTGCCGGAGTGAGCCGCCGCAGATAAGAGCGGACCATTTCGTAAGGGCCAATCAGGATGATTCCGACCGACTCAGGAGTAGTGGCGTGCTATTTCTGGAGAACGAAGGGGCTCCCGACCGATTCCGCTAAGACAATCGGGTGGATTGCGGTCCGGGACGGGGAAAATGAGTTTGATGCCGTCAATGA")
    
    # Call the middle_edge function
    edge = middle_edge(s, t, match, mismatch, indel)
    print(f"{edge[0][0]} {edge[0][1]}")
    print(f"{edge[1][0]} {edge[1][1]}")

if __name__ == "__main__":
    main()
