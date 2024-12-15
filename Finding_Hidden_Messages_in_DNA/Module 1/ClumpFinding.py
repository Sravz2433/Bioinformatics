def ClumpFinding(genome, k, t, L):
    counts = dict()
    for i in range(L):
        text = genome[i:(i+k)]
        counts[text] = counts.get(text, 0) + 1
    clump = [p for p, v in counts.items() if v >= t]
    for i in range(1, len(genome)-L+1):
        firstPattern = genome[(i-1):(i-1+k)]
        counts[firstPattern] -= 1
        lastPattern = genome[(i+L-k):(i+L)]
        counts[lastPattern] = counts.get(lastPattern, 0) + 1
        if counts[lastPattern] >= t and lastPattern not in clump:
            clump.append(lastPattern)
    return clump

text = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
k = 5
L =50
t = 4
clump = ClumpFinding(text, k, t, L)
print(' '.join(clump))