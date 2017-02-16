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
import math


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

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

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False


def question3(G):
    if not G:
        return {}
    # Take the input adjacency list and parse it to a graph
    graph = to_graph(G)
    return to_adjacency_list( find_MST(graph) )


# This function takes a graph and returns the Minimum Spaning Tree (MST) of that graph, also in the form of a graph
def find_MST(G):
    mst = Graph()

    node = G.nodes[0]
    G._clear_visited()
    queue = []
    def enqueue(n, q=queue):
            n.visited = True
            q.append(n)
    def unvisited_outgoing_edge(n, e):
            return ((e.node_from.value == n.value) and
                    (not e.node_to.visited))

    
    enqueue(node, queue)
    visited = [node.value]
    while queue:
        node = queue[-1]

        # Calculate all the possible edges from the nodes already visited
        pos_edges = []
        for e in queue:
            pos_edges.extend(e.edges)
        
        possible_edges = [x for x in pos_edges if not x.node_to.visited]
        # if there are no possible edges from the current node, pop it from the stack
 
        min_edge = None
        if not possible_edges:
            queue.pop()
            pass
        else:
            min_edge = min(possible_edges, key=lambda x: x.value )

        if min_edge:
            mst.insert_edge(min_edge.value, min_edge.node_from.value, min_edge.node_to.value)
            node = min_edge.node_to
            enqueue(node, queue)

    return mst


def find_MST_helper(G):
    pass

# This function takes an adjacency list and returns a graph
def to_graph(G):
    graph = Graph()

    for entry in G:
        node = Node(entry)

        # Insert edges associated with the node created
        for edge in G[node.value]:
            graph.insert_edge(edge[1], node.value, edge[0])
    return graph

# This function takes a graph and return a adjacency list 
def to_adjacency_list2(G):
    Alist = {}
    for node in G.nodes:

        Alist[node.value] = []
        for edge in node.edges:

            Alist[node.value].append( (edge.node_to.value, edge.value) )

    return Alist

def to_adjacency_list(G):
    Alist = {}
    # Populate the adjacency table
    for node in G.nodes:
        Alist[node.value] = []

    for node in G.nodes:
        edges = [x for x in node.edges if not x.node_to.value == node.value]


        for edge in edges:
            Alist[node.value].append( (edge.node_to.value, edge.value) )
            # Make sure to also include the inverse edge
            Alist[edge.node_to.value].append( (edge.node_from.value, edge.value) )
    return Alist


test = {'A': [('B', 2)],
         'B': [('A', 2), ('C', 5)], 
         'C': [('B', 5)]}

print question3(test)
print test

test = {'A': [('B', 2)],
          'B': [('A', 2), ('C', 5), ('D', 3)],
          'C': [('B', 5), ('D', 3)]}
print question3(test)

test = {'A': [('B', 2), ('C', 1)],
          'B': [('A', 2), ('C', 5), ('D', 3)],
          'C': [('B', 5), ('D', 3), ('A', 1)]}
print question3(test)

test = {}
print question3(test)



