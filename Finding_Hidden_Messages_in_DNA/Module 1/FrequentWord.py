def frequency_table(text, k):
    """Compute the frequency table of all k-mers in the text."""
    freq_map = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        if kmer in freq_map:
            freq_map[kmer] += 1
        else:
            freq_map[kmer] = 1
    return freq_map

def better_frequent_words(text, k):
    """Find the most frequent k-mers in the given text."""
    frequent_patterns = []  # Initialize an empty list
    freq_map = frequency_table(text, k)  # Compute the frequency table
    max_freq = max(freq_map.values())  # Find the maximum frequency
    
    # Find all k-mers with the maximum frequency
    for pattern, frequency in freq_map.items():
        if frequency == max_freq:
            frequent_patterns.append(pattern)
    
    return frequent_patterns

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
result = better_frequent_words(text, k)
print("Most frequent k-mers:", result)
