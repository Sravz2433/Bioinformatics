
from sys import argv
from random import randint
"""
CODE CHALLENGE: Solve the Eulerian Cycle Problem.
     Input: The adjacency list of an Eulerian directed graph.
     Output: An Eulerian cycle in this graph.

Sample Input:
     0 -> 3
     1 -> 0
     2 -> 1,6
     3 -> 2
     4 -> 2
     5 -> 4
     6 -> 5,8
     7 -> 9
     8 -> 7
     9 -> 6

Sample Output:
     6->8->7->9->6->5->4->2->1->0->3->2->6
     """



def find_eulerian_tour(graph):
    vertices = graph

    print("vertices", vertices)
    start = []

    maxGraph = max(graph.keys())
    start_vertex = randint(0, maxGraph)
    # Choose a starting vertex v and follow a trail of edges from that vertex until returning to v.
    start.append(list(vertices.keys())[start_vertex])
    print(start)

    stack = [start[0]]  # a list containing the vertices in the current tour with unused edges
    tour = []  # a list containing the final tour

    while stack:
        v = stack[-1]  # select the starting vertex
        if vertices[v]:  # if there are unused edges from the starting vertex
            w = vertices[v][0]  # select the vertex connected by the first unused edge
            stack.append(w)  # add the new vertex to the stack, to become the new starting vertex
            print("stack ", stack)
            del vertices[v][0]  # delete edge v-w from the graph
        else: 
            # if there are no unused edges from the starting vertex, remove it from the stack
            # and add it to the final tour
            tour.append(stack.pop())
    print("---------\n---------\n--------\n")
    return tour



def main(argv):
    path = []
    with open(argv[1], "r") as fstream:
        path = [line.strip() for line in fstream.readlines()]

    print("Input graph:", path)

    graph = {}
    for line in path:
        vertex, neighbors = line.split(": ")
        vertex = int(vertex)
        graph[vertex] = list(map(int, neighbors.split(' ')))

    final = find_eulerian_tour(graph)
    print(' '.join(map(str, final[::-1])))

if __name__ == "__main__":
    main(argv)
