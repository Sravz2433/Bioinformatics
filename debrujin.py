def de_bruijn_from_kmers(kmers):
    adjacency = {}
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        adjacency.setdefault(prefix, []).append(suffix)
    return adjacency

# Replace 'input_kmers.txt' with the path to your file
input_file = 'input.txt'
output_file= 'output.txt'

# Read k-mers from file
kmers = []
with open(input_file, 'r') as f:
    for line in f:
        # Strip and split the line by whitespace to get individual k-mers
        kmers.extend(line.strip().split())

# Construct the De Bruijn graph
graph = de_bruijn_from_kmers(kmers)

# Print the adjacency list\
with open(output_file, 'w') as f:
    for prefix in sorted(graph.keys()):
        print(f"{prefix}: {' '.join(graph[prefix])}", file=f)
