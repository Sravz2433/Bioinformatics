import random

def random_walk(graph, start):
    cycle = [start]
    current_node = start
    
    while True:
        neighbors = graph[current_node]
        unexplored_edges = [neighbor for neighbor in neighbors if (current_node, neighbor) in graph[current_node]]
        
        if unexplored_edges:
            next_node = random.choice(unexplored_edges)
            graph[current_node].remove((current_node, next_node))
            cycle.append(next_node)
            current_node = next_node
        else:
            break
    
    return cycle

def eulerian_cycle(graph):
    start_node = list(graph.keys())[0]
    cycle = random_walk(graph, start_node)
    
    while any(graph[node] for node in cycle):
        new_start = [node for node in cycle if graph[node]]
        new_start = random.choice(new_start)
        
        index = cycle.index(new_start)
        cycle = cycle[index:] + cycle[:index]
        
        new_cycle = random_walk(graph, new_start)
        cycle_index = cycle.index(new_start)
        cycle = cycle[:cycle_index] + new_cycle + cycle[cycle_index+1:]
    
    return cycle

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print(eulerian_cycle(graph))
