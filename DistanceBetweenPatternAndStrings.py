def HammingDistance(pattern1, pattern2):
    # Function to calculate Hamming distance between two strings
    return sum(c1 != c2 for c1, c2 in zip(pattern1, pattern2))

def DistanceBetweenPatternAndStrings(pattern, dna):
    k = len(pattern)
    distance = 0

    for text in dna:
        hamming_distance = float('inf')  # Initialize with infinity
        for i in range(len(text) - k + 1):
            pattern_prime = text[i:i + k]
            current_distance = HammingDistance(pattern, pattern_prime)
            hamming_distance = min(hamming_distance, current_distance)

        distance += hamming_distance

    return distance

# Example usage:
pattern = "AGCCC"

with open('C:/Users/sravy/Downloads/dataset_30312_1 (2).txt', 'r') as dna_f:
    dna = [line.strip() for line in dna_f]

# Sample Output
result = DistanceBetweenPatternAndStrings(pattern, dna)
print(result)
