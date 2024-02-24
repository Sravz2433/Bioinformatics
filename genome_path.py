def concatenate_genome_path(strings):
    genome_path = strings[0]
    for i in range(1, len(strings)):
        genome_path += strings[i][-1]
    return genome_path

with open("C:/Users/sravy/Downloads/dataset_30182_3 (6).txt", 'r') as txt:
    strings = txt.read().strip().split(" ")


genome_path = concatenate_genome_path(strings)
with open('genome_path.txt', 'w') as file:
    file.write(genome_path)