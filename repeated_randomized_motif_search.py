import random

def profile_most_probable_kmer(text, k, profile):
    max_prob = -1
    most_probable = ""
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = 1
        for j in range(len(kmer)):
            if kmer[j] == 'A':
                prob *= profile[0][j]
            elif kmer[j] == 'C':
                prob *= profile[1][j]
            elif kmer[j] == 'G':
                prob *= profile[2][j]
            elif kmer[j] == 'T':
                prob *= profile[3][j]
        if prob > max_prob:
            max_prob = prob
            most_probable = kmer
    return most_probable

def profile_matrix(motifs, pseudocount=1):
    k = len(motifs[0])
    profile = [[pseudocount] * k for _ in range(4)]
    for motif in motifs:
        for i in range(k):
            if motif[i] == 'A':
                profile[0][i] += 1
            elif motif[i] == 'C':
                profile[1][i] += 1
            elif motif[i] == 'G':
                profile[2][i] += 1
            elif motif[i] == 'T':
                profile[3][i] += 1
    total = [sum(row) for row in profile]
    for i in range(4):
        for j in range(k):
            profile[i][j] /= total[i]
    return profile

def randomized_motif_search(dna, k, t):
    best_motifs = []
    for seq in dna:
        rand_index = random.randint(0, len(seq) - k)
        best_motifs.append(seq[rand_index:rand_index+k])
    while True:
        profile = profile_matrix(best_motifs)
        motifs = [profile_most_probable_kmer(seq, k, profile) for seq in dna]
        if motifs == best_motifs:
            return best_motifs
        else:
            best_motifs = motifs

def repeated_randomized_motif_search(dna, k, t, num_trials=1000):
    best_score = float('inf')
    best_motifs = None
    for _ in range(num_trials):
        motifs = randomized_motif_search(dna, k, t)
        score = score_motifs(motifs)
        if score < best_score:
            best_score = score
            best_motifs = motifs
    return best_motifs

def score_motifs(motifs):
    consensus = consensus_sequence(motifs)
    score = 0
    for motif in motifs:
        for i in range(len(motif)):
            if motif[i] != consensus[i]:
                score += 1
    return score

def consensus_sequence(motifs):
    k = len(motifs[0])
    consensus = ""
    for j in range(k):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            count[motif[j]] += 1
        consensus += max(count, key=count.get)
    return consensus

# Example usage:
k = 15
t = 20
with open("C:/Users/sravy/Downloads/dataset_30307_5 (2).txt", 'r') as dna_f:
    dna = [line.strip() for line in dna_f]
best_motifs = repeated_randomized_motif_search(dna, k, t)
print(*best_motifs, sep=' ')
