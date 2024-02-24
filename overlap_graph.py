def overlap_graph(patterns):
    adjacency_list = {}

    # Create a dictionary to store k-mers as keys and their suffixes as values
    suffixes = {}
    for pattern in patterns:
        suffixes[pattern] = pattern[1:]

    # For each k-mer, find its overlaps with other k-mers
    for pattern in patterns:
        prefix = pattern[:-1]  # Get the prefix of the current k-mer
        for other_pattern, suffix in suffixes.items():
            if prefix == suffix:  # Check if the prefix of the current k-mer matches the suffix of another k-mer
                if pattern not in adjacency_list:
                    adjacency_list[pattern] = [other_pattern]
                else:
                    adjacency_list[pattern].append(other_pattern)

    return adjacency_list

# Example usage:
with open('C:/Users/sravy/Downloads/dataset_30278_10 (2).txt', 'r') as file:
    patterns = file.read()
overlap = overlap_graph(patterns)
for node, edges in overlap.items():
    print(f"{node}: {' '.join(edges)}")