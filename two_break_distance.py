def parse_genome(genome):
    """Parses a genome string into a list of chromosomes."""
    chromosomes = genome.strip().split(')(')
    chromosomes[0] = chromosomes[0][1:]
    chromosomes[-1] = chromosomes[-1][:-1]
    return [list(map(int, chromosome.split())) for chromosome in chromosomes]

def create_edges(genome):
    """Creates edges for the breakpoint graph of a genome."""
    edges = []
    for chromosome in genome:
        for i in range(len(chromosome)):
            if i == len(chromosome) - 1:  # last gene, circular wrap to first
                edge = (chromosome[i], -chromosome[0])
            else:
                edge = (chromosome[i], -chromosome[i + 1])
            edges.append(edge)
    return edges

def breakpoint_graph(P, Q):
    """Constructs the breakpoint graph from genomes P and Q."""
    P_edges = create_edges(parse_genome(P))
    Q_edges = create_edges(parse_genome(Q))
    return P_edges + Q_edges

def find_cycles(edges):
    """Finds all cycles in the breakpoint graph."""
    visited = set()
    cycles = []

    def explore(edge):
        """Recursively explores all edges to find cycles."""
        current_cycle = []
        stack = [edge]
        while stack:
            e = stack.pop()
            if e not in visited:
                visited.add(e)
                current_cycle.append(e)
                next_edge = (-e[1], e[0])  # next edge to continue cycle
                if next_edge not in visited and next_edge in edges:
                    stack.append(next_edge)
        return current_cycle

    for edge in edges:
        if edge not in visited:
            cycle = explore(edge)
            if cycle:
                cycles.append(cycle)

    return cycles

def two_break_distance(P, Q):
    """Computes the 2-break distance between genomes P and Q."""
    # Number of blocks
    num_blocks = sum(len(chromosome) for chromosome in parse_genome(P))

    # Construct breakpoint graph and find number of cycles
    bg = breakpoint_graph(P, Q)
    cycles = find_cycles(bg)

    # Compute the 2-break distance
    distance = num_blocks - len(cycles)
    return distance

# Example Input
P = "(+1 +2 +3 +4 +5 +6)"
Q = "(+1 -3 -6 -5)(+2 -4)"

# Calculate 2-Break Distance
result = two_break_distance(P, Q)
print(result)
