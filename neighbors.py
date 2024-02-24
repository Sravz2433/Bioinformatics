def hamming_distance(str1, str2):
    # Calculate the Hamming distance between two strings
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

def neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    
    nucleotides = ['A', 'C', 'G', 'T']
    neighborhood = []
    suffix = pattern[1:]
    suffix_neighbors = neighbors(suffix, d)  # Recursive call
    
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in nucleotides:
                neighborhood.append(pattern[0] + text)
        else:
            neighborhood.append(pattern[0] + text)
    
    return neighborhood

text = 'ACG'
d = 1

result = neighbors(text, d)

with open('neighbors.txt', 'w') as f:
    for neighborhood in result:
        f.write(neighbors + '\n')

