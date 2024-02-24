from collections import defaultdict

def hamming_distance(str1, str2):
    # Calculate the Hamming distance between two strings
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

def generate_neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']

    nucleotides = ['A', 'C', 'G', 'T']
    neighbors = set()

    suffix_neighbors = generate_neighbors(pattern[1:], d)
    for neighbor in suffix_neighbors:
        if hamming_distance(pattern[1:], neighbor) < d:
            for nucleotide in nucleotides:
                neighbors.add(nucleotide + neighbor)
        else:
            neighbors.add(pattern[0] + neighbor)

    prefix_neighbors = generate_neighbors(pattern[:-1], d)
    for neighbor in prefix_neighbors:
        if hamming_distance(pattern[:-1], neighbor) < d:
            for nucleotide in nucleotides:
                neighbors.add(neighbor + nucleotide)
        else:
            neighbors.add(neighbor + pattern[-1])

    return list(neighbors)

def reverse_complement(pattern):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement[base] for base in reversed(pattern))

def frequent_words_with_mismatches_and_reverse_complements(text, k, d):
    kmer_counts = defaultdict(int)
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        kmer_neighbors = generate_neighbors(kmer, d)
        for neighbor in kmer_neighbors:
            kmer_counts[neighbor] += 1
            kmer_counts[reverse_complement(neighbor)] += 1
    
    max_count = max(kmer_counts.values())
    frequent_kmers = [kmer for kmer, count in kmer_counts.items() if count == max_count]
    
    return frequent_kmers

with open('C:/Users/sravy/Downloads/dataset_30278_10 (2).txt', 'r') as file:
    text = file.read().strip()
k = 7
d = 2
result = frequent_words_with_mismatches_and_reverse_complements(text, k, d)
for kmer in result:
    print(kmer)
