import numpy as np

def minimum_skew(genome):
    skew = np.zeros(len(genome)+1)
    for i in range(1, len(genome)+1):
        if genome[i-1] == 'G':
            skew[i] = skew[i-1] + 1
        elif genome[i-1] == 'C':
            skew[i] = skew[i-1] - 1
        else:
            skew[i] = skew[i-1]
    min_skew = np.where(skew == np.min(skew))
    return min_skew[0]

# Open the file for reading
with open('C:\\Users\\sravy\\Downloads\\dataset_30277_10 (5).txt', 'r') as file:
    genome = file.read().strip()

result = minimum_skew(genome)

# Convert the result to a string format
result_str = ' '.join(map(str, result))

# Open a file for writing the result
with open('minimum_skew.txt', 'w') as file:
    file.write(result_str)
