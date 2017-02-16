#quesiton3

# Question 3
# Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

input1 = {'A': [('B', 2)],
          'B': [('A', 2), ('C', 5)],
          'C': [('B', 5)]}
input2 = {'A': [('B', 2)],
          'B': [('A', 2), ('C', 5), ('D', 3)],
          'C': [('B', 5), ('D', 3)]}
input3 = {'A': [('B', 2), ('C', 1)],
          'B': [('A', 2), ('C', 5), ('D', 3)],
          'C': [('B', 5), ('D', 3), ('A', 1)]}
# Vertices are represented as unique strings. The function definition should be question3(G)


def question3(G):
    edges_to_add = parse_adj_list(G)
    graph = Graph()
    for edge in edges_to_add:
        graph.insert_edge(edge[0], edge[1], edge[2])
    return graph.create_prims_mst()


def parse_adj_list(adj_list):
    edges = []
    for parent, children in adj_list.iteritems():
        for child in children:
            edges.append((child[1], parent, child[0]))
    return edges


# Sourced Node class declaration from the Udacity Technical
# Interview Practice course materials
class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

# Sourced Edge class declaration from the Udacity Technical
# Interview Practice course materials
class Edge(object):
    def __init__(self, value, parent, child):
        self.value = value
        self.parent = parent
        self.child = child

# Sourced Graph, insert_node and insert_edge logic from
# the Udacity Technical Interview Practice course materials
class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.seen = False

    def insert_node(self, val):
        new_node = Node(val)
        self.nodes.append(new_node)
        return new_node

    def insert_edge(self, val, parent, child):
        nodes = {parent: None, child: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_parent = nodes[parent]
        node_child = nodes[child]
        new_edge = Edge(val, node_parent, node_child)
        node_parent.edges.append(new_edge)
        node_child.edges.append(new_edge)
        self.edges.append(new_edge)

    def create_prims_mst(self):
        mst_nodes = [self.nodes[0]]
        mst_node_vals = [self.nodes[0].value]
        mst_edges = []

        while len(mst_nodes) < len(self.nodes):
            edges = []
            new_node = None
            for node in mst_nodes:  # Build list of possible edges
                for edge in node.edges:
                    par = edge.parent.value
                    chi = edge.child.value
                    if par not in mst_node_vals or chi not in mst_node_vals:
                        edges.append(edge)
            edges.sort(key=lambda edge: edge.value)  # Find lowest val edge
            new_edge = edges[0]
            mst_edges.append(new_edge)
            if new_edge.child.value not in mst_node_vals:
                mst_nodes.append(new_edge.child)
                mst_node_vals.append(new_edge.child.value)
            else:
                mst_nodes.append(new_edge.parent)
                mst_node_vals.append(new_edge.parent.value)

        return self._build_adj_table(mst_edges)

    def _build_adj_table(self, edges):
        results = {}
        for edge in edges:
            par = edge.parent
            chi = edge.child
            if edge.parent.value in results:
                results[edge.parent.value].append((edge.value, edge.child.value))
            else:
                results[edge.parent.value] = [(edge.value, edge.child.value)]

            if edge.child.value in results:
                results[edge.child.value].append((edge.value, edge.parent.value))
            else:
                results[edge.child.value] = [(edge.value, edge.parent.value)]
        return results


if __name__ == '__main__':
    print '======'
    print 'TEST 1: Create MST for:'
    print input1
    print 'Result should be identical to input'
    print question3(input1)
    print '======'
    print 'TEST 2: Create MST for:'
    print input2
    print 'Result should ignore connection between B and C'
    print question3(input2)
    print '======'
    print 'TEST 3: Create MST for:'
    print input3
    print 'Result should connect A to C, and should ignore connection between B and C'
    print question3(input3)
    print '======'


# Notes
#
# This program implements Prim's algorithm to find the minimum spanning tree
# between nodes in a provided adjacency list. It then returns a new adjacency
# list corresponding to the connections formed by the minimum spanning tree.
#
# First the algorithm parses the input into triples that can be used to
# create edges in a graph. It then uses those commands to build a graph with
# connecting Node and Edge objects. Once the graph is instantiated, a MST
# is created within the graph itself.
#
# To implement Prim's algorithm, a graph node is arbitrarily selected, and
# a while loop examines all of the edges attached to that node. Of those
# edges, the edge with the smallest value, and its new connecting node, are
# appended to the MST. When examining connections, if a connection is
# found to link between two nodes which are already part of the MST,
# it is ignored.
#
# This process repeats, adding nodes, determining connecting edges, selecting
# the smallest value edge, and appending nodes until all nodes have been added
# to the MST.
#
# This implementation of Prim's algorithm is limited by the sorting algorithm
# used to determine the minimum elegible edge. Because Python's .sort()
# implementation runs at O(n log n), it is also the average time complexity
# of the overall algorithm. The algorithm's worst case space complexity is
# aproximately O(n) where n is the number of adjacencies in the input adjacency
# list. The true space complexity is much closer to O(2n + n) due to the need for
# nodes and edges to connect them. However, this aproximates to O(n).
