def trie_construction(patterns):
    trie = {}
    new_node = 0
    
    # Initialize root
    trie[new_node] = {}
    
    # Iterate over each pattern
    for pattern in patterns:
        current_node = 0
        for symbol in pattern:
            # If there is no edge labeled with 'symbol', create it
            if symbol not in trie[current_node]:
                new_node += 1
                trie[current_node][symbol] = new_node
                trie[new_node] = {}  # Create a new node in the trie
            # Move to the next node
            current_node = trie[current_node][symbol]
    
    # Prepare the adjacency list in the required format
    adjacency_list = []
    # Iterate over the nodes
    for node in trie:
        # Iterate over the edges (symbols) for each node
        for symbol, next_node in trie[node].items():
            adjacency_list.append((node, next_node, symbol))
    
    return adjacency_list

# Input
patterns = input().split()

# Get the adjacency list representation of the Trie
adj_list = trie_construction(patterns)

# Output the adjacency list
with open("output.txt", "w") as file:
    for edge in adj_list:
        # Write each edge in the desired format to the file
        file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")

