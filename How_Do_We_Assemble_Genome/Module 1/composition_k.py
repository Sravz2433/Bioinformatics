def concatenate_genome_path(strings):
    genome_path = strings[0]
    for i in range(1, len(strings)):
        genome_path += strings[i][-1]
    return genome_path

# Example usage:
strings = ["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"]
genome_path = concatenate_genome_path(strings)
print(genome_path)
k = 100
with open('E:/HTML/bioinformatics/composition_k.txt', 'r') as file:
    text = file.read().strip()
result = composition_k(k, text)
result= ' '.join(map(str, result))
result_str = ''.join(map(str, result))
with open('composition_k_1.txt', 'w') as file:
    file.write(result)
