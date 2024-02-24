import numpy as np

def hamming_distance(pattern1, pattern2):
    """
    Calculate the Hamming distance between two strings of equal length.
    """
    distance = 0
    for i in range(len(pattern1)):
        if pattern1[i] != pattern2[i]:
            distance += 1
    return distance

def profile_most_probable_kmer(text, k, profile):
    """
    Find the profile-most probable k-mer in a given string based on a profile matrix.
    """
    max_prob = -1
    most_probable_kmer = ""

    # Iterate over all k-mers in the text
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = 1
        # Calculate the probability of the k-mer based on the profile matrix
        for j in range(k):
            nucleotide = kmer[j]
            if nucleotide == 'A':
                prob *= profile[0][j]
            elif nucleotide == 'C':
                prob *= profile[1][j]
            elif nucleotide == 'G':
                prob *= profile[2][j]
            elif nucleotide == 'T':
                prob *= profile[3][j]
        # Update the most probable k-mer if the current k-mer has a higher probability
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer

    return most_probable_kmer

def profile_matrix_with_pseudocounts(motifs):
    """
    Generate a profile matrix with pseudocounts from a collection of motifs.
    """
    k = len(motifs[0])
    profile = np.zeros((4, k))

    for i in range(k):
        count = {'A': 1, 'C': 1, 'G': 1, 'T': 1}  # Initialize count with pseudocounts
        for motif in motifs:
            count[motif[i]] += 1
        for j in range(4):
            profile[j][i] = count['ACGT'[j]] / (len(motifs) + 4)  # Add pseudocounts to the denominator

    return profile

def greedy_motif_search_with_pseudocounts(dna, k, t):
    best_motifs = [text[:k] for text in dna]
    n = len(dna[0])

    for i in range(n - k + 1):
        motifs = [dna[0][i:i+k]]  # Initialize motifs with the first k-mer in the first string
        for j in range(1, t):
            profile = profile_matrix_with_pseudocounts(motifs)
            motifs.append(profile_most_probable_kmer(dna[j], k, profile))
        if score_motifs(motifs) < score_motifs(best_motifs):
            best_motifs = motifs

    return best_motifs

def score_motifs(motifs):
    """
    Calculate the score of a collection of motifs.
    """
    consensus = consensus_sequence(motifs)
    score = 0
    for motif in motifs:
        score += hamming_distance(consensus, motif)
    return score

def consensus_sequence(motifs):
    """
    Generate a consensus sequence from a collection of motifs.
    """
    k = len(motifs[0])
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    consensus = ""

    for j in range(k):
        for motif in motifs:
            count[motif[j]] += 1
        consensus += max(count, key=count.get)
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    return consensus

# Example usage:
k = 12
t = 25
with open('C:/Users/sravy/Downloads/dataset_30306_9 (1).txt', 'r') as dna_f:
    dna = [line.strip() for line in dna_f]
best_motifs = greedy_motif_search_with_pseudocounts(dna, k, t)
print(*best_motifs,sep=" ")
