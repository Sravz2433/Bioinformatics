def read_graph_from_file(filename):
    """
    Reads the graph adjacency list from a file.
    Each line of the file should represent a node and its adjacent nodes in the format: "node: adjacent1 adjacent2 ..."
    """
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            node = int(parts[0])
            adjacent_nodes = list(map(int, parts[1].split()))
            graph[node] = adjacent_nodes
    return graph

def MaximalNonBranchingPaths(Graph):
    Paths = []  # Initialize the list to store paths

    # A helper function to determine if a node is 1-in-1-out
    def is_1_in_1_out(node):
        # Check if the node exists in the graph and if it's a 1-in-1-out node
        return node in Graph and len(Graph[node]) == 1 and sum(node in edges for edges in Graph.values()) == 1

    # Step 1: Find non-branching paths starting from non-1-in-1-out nodes
    for v in Graph:
        if not is_1_in_1_out(v):  # If v is not a 1-in-1-out node
            if v in Graph and len(Graph[v]) > 0:  # If v has outgoing edges
                for w in Graph[v]:
                    NonBranchingPath = [v, w]  # Start a new path
                    while is_1_in_1_out(w):  # While w is a 1-in-1-out node
                        u = Graph[w][0]  # Get the next node
                        NonBranchingPath.append(u)
                        w = u  # Move to the next node
                    Paths.append(NonBranchingPath)  # Add the path to Paths

    # Step 2: Find isolated cycles
    visited = set()

    def find_cycle(start):
        cycle = []
        current = start
        while current not in visited:
            visited.add(current)
            cycle.append(current)
            next_node = Graph[current][0]
            current = next_node
        cycle.append(current)  # To complete the cycle
        return cycle

    for v in Graph:
        if is_1_in_1_out(v) and v not in visited:
            cycle = find_cycle(v)
            if cycle[0] == cycle[-1]:  # Ensure it is a complete cycle
                Paths.append(cycle[:-1])  # Add the cycle to Paths

    return Paths

# Example usage
filename = ""  # Update with your input file path
graph = {}
with open("C:/Users/sravy/Downloads/dataset_30209_2 (2).txt", 'r') as file:
    for line in file:
        parts = line.strip().split(':')
        node = int(parts[0])
        adjacent_nodes = list(map(int, parts[1].split()))
        graph[node] = adjacent_nodes

paths = MaximalNonBranchingPaths(graph)
for path in paths:
    print(" ".join(map(str, path)))
