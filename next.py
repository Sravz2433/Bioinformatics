from collections import defaultdict, deque

def build_de_bruijn_graph(kmers):
    graph = defaultdict(list)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
    return graph

def find_eulerian_path(graph):
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    # Calculate in-degrees and out-degrees
    for node in graph:
        for neighbor in graph[node]:
            out_degree[node] += 1
            in_degree[neighbor] += 1
    
    start_node = None
    end_node = None
    
    # Find start and end nodes
    for node in set(in_degree.keys()).union(out_degree.keys()):
        if out_degree[node] > in_degree[node]:
            start_node = node
        if in_degree[node] > out_degree[node]:
            end_node = node
    
    if start_node is None:
        start_node = next(iter(graph.keys()))
    
    stack = [start_node]
    path = deque()
    
    while stack:
        node = stack[-1]
        if graph[node]:
            next_node = graph[node].pop()
            stack.append(next_node)
        else:
            path.appendleft(stack.pop())
    
    return list(path)

def reconstruct_string_from_kmers(kmers):
    graph = build_de_bruijn_graph(kmers)
    path = find_eulerian_path(graph)
    
    # Reconstruct the string from the Eulerian path
    reconstructed_string = path[0]
    for node in path[1:]:
        reconstructed_string += node[-1]
    
    return reconstructed_string

# Read input
k = int(input().strip())
kmers = []
for _ in range(k):
    kmers.append(input().strip())

# Reconstruct the string
reconstructed_string = reconstruct_string_from_kmers(kmers)
print(reconstructed_string)
