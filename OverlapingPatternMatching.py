def OverlappingPatternMatching(Pattern, Genome):
    positions = []
    pattern_length = len(Pattern)
    genome_length = len(Genome)
    for i in range(genome_length - pattern_length + 1):
        if Genome[i:i + pattern_length] == Pattern:
            positions.append(i)
    return positions


with open('C:/Users/sravy/Downloads/dataset_30273_5 (7).txt', 'r') as file:
    text = file.read()
Pattern = "TGAAAGTTG"
matches = OverlappingPatternMatching(Pattern, text)
result = ' '.join(map(str, matches))

with open('OverlappingPatternMatching.txt', 'w') as file:
    file.write(result)

print("Found positions are uploaded in OverlappingPatternMatching.txt")