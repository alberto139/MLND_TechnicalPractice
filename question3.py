# Question 3
# Given an undirected graph G, find the minimum spanning tree within G. 
# A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges.
# Your function should take in and return an adjacency list structured like this:

#{'A': [('B', 2)],
# 'B': [('A', 2), ('C', 5)], 
# 'C': [('B', 5)]}
#Vertices are represented as unique strings. The function definition should be question3(G)

# This question is answered by finding the minimum spanning tree of the graph.
# To do this, Prim's algorithm will be used.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, parent, child):
        self.value = value
        self.parent = parent
        self.child = child

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.seen = False

    def insert_node(self, val):
        new_node = Node(val)
        self.nodes.append(new_node)
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

test1 = {'A': [('B', 2)],
         'B': [('A', 2), ('C', 5)], 
         'C': [('B', 5)]}

def question3(G):
    if not G:
        return {}
    # Take the input adjacency list and parse it to a graph
    graph = to_graph(G)


def to_graph(G):
    graph = Graph()
    for entry in G:
        node = Node(entry)
        graph.insert_node(node)
    #print graph.nodes



print question3(test1)

