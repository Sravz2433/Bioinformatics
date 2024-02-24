def FrequencyTable(Text, k):
    freqMap = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        if Pattern in freqMap:
            freqMap[Pattern].append(i)
        else:
            freqMap[Pattern] = [i]
    return freqMap

def ReverseComplement(Pattern):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp = ''.join(complement[base] for base in reversed(Pattern))
    return reverse_comp

def FindClumps(Text, k, L, t):
    Patterns = set()
    n = len(Text)
    for i in range(n - L + 1):
        Window = Text[i:i + L]
        freqMap = FrequencyTable(Window, k)
        for pattern, positions in freqMap.items():
            if len(positions) >= t:
                for j in range(len(positions) - t + 1):
                    if positions[j + t - 1] - positions[j] <= L - k:
                        Patterns.add(pattern)
                        break
        reverse_window = ReverseComplement(Window)
        freqMap_reverse = FrequencyTable(reverse_window, k)
        for pattern, positions in freqMap_reverse.items():
            if len(positions) >= t:
                for j in range(len(positions) - t + 1):
                    if positions[j + t - 1] - positions[j] <= L - k:
                        Patterns.add(ReverseComplement(pattern))
                        break
    return ' '.join(sorted(Patterns))

# Example usage:
Text = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
k = 5
L = 50
t = 4
print(FindClumps(Text, k, L, t))
