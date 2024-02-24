def PatternMatching(Pattern, Genome):
    positions = []
    pattern_length = len(Pattern)
    genome_length = len(Genome)
    for i in range(genome_length - pattern_length + 1):
        if Genome[i:i + pattern_length] == Pattern:
            positions.append(i)
    return positions

Pattern = "CCTCCCACC"
with open('C:/users/sravy/Downloads/dataset_30273_5 (4).txt','r') as file:
    Genome = file.read()

matches = PatternMatching(Pattern, Genome)

print(*matches, sep=' ')

