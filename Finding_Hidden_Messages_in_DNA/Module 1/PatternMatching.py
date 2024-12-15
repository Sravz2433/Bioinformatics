def find_pattern_occurrences(pattern, genome):
    matches = []
    pattern_length = len(pattern)
    genome_length = len(genome)

    for i in range(genome_length - pattern_length + 1):
        if genome[i:i + pattern_length] == pattern:
            matches.append(i)

    return matches

pattern = "ATA"
genome = "GACGATATACGACGATA"

positions = find_pattern_occurrences(pattern, genome)
print(" ".join(map(str, positions)))
