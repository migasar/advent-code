"""Day 15: Chiton"""

import pathlib
import sys


# Get Input
INPUT_EX = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


# Set Input
puzzle_input = INPUT_EX

# Format Input
def parse_input(puzzle_input):
    """Parse input"""

    return None


# Part 1
# The solution is based on an implementation of the Algorithm of Dijkstra.
# It builds a search graph to find the shortest path between two nodes.

class Graph():

    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)


    def construct_graph(self, nodes, init_graph):
        """ This methode makes sure that the graph is symmetrical.
            In other words, if there's a path from node A to B with a value V,
            there needs to be a path from node B to node A with a value V.
        """

        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph


    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes


    def get_outgoing_edges(self, node):
        "Returns the neighbours of a node."

        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)

        return connections


    def value(self, node_1, node_2):
        "Returns the value of aan edge between two nodes."
        return self.graph[node_1][node_2]




# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and
                sptSet[v] == False and
                dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

g.dijkstra(0)

# This code is contributed by Divyanshu Mehta





def part1(data):
    """Solve part 1"""

    return None


def part2(data):
    """Solve part 2"""

    return None


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_input(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2
