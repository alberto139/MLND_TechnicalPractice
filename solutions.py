# Question 1 
# Given two strings s and t, determine whether some anagram of t is a substring of s. 
# For example: if s = "udacity" and t = "ad", then the function returns True. 
# Your function definition should look like: question1(s, t) and return a boolean True or False.
def question1(s,t):

	for char in t:
		if char in s:
			s = s.replace(char, '', 1)
			t = t.replace(char, '', 1)
	if not t:
		return True
	return False

# Question 2
# Given a string a, find the longest palindromic substring contained in a. 
# Your function definition should look like question2(a), and return a string.
# NOTE: For quetions 1 and 2 it might be useful to have a function that returns all substrings...
def question2(a):
	longest_pal = ''

	# Base Case: The initial string is a plindrome
	if isPalindrome(a):
		return a

	end = len(a)
	start = 0

	# Get all the substrings and check if its a palindrome
	# if it is a palindrome and it's longer than longest_pal
	# make longest_pal the current substring
	while start != end:

		while end != start:

			if isPalindrome( a[start:end] ) and  len( a[start:end] ) >= len( longest_pal ):
				longest_pal = a[start:end]
			end -= 1

		start += 1
		end = len(a)

	return longest_pal

# Helper function for question 2
# Determine if a string s is a palindrome
def isPalindrome(s):
	# Base Case: if s empty
	if not s:
		return True
	# Bsae Case: is s is a single character
	#print (len(s) == 1)
	if len(s) == 1:
		return True

	if s[0] == s[-1]:
		return isPalindrome(s[1:-1])
	return False

class GraphNode(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

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
        new_node = GraphNode(val)
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


class GraphNode(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

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
        new_node = GraphNode(val)
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
        node = GraphNode(entry)

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


#Question 4
# Find the least common ancestor between two nodes on a binary search tree. 
# The least common ancestor is the farthest node from the root that is an ancestor of both nodes. 
# For example, the root is a common ancestor of all nodes on the tree, 
# but if both nodes are descendents of the root's left child, 
# then that left child might be the lowest common ancestor. 
# You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. 
# The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, 
# where the index of the list is equal to the integer stored in that node and a 1 represents a child node, 
# r is a non-negative integer representing the root, 
# and n1 and n2 are non-negative integers representing the two nodes in no particular order. 
# For example, one test case might be

# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = TreeNode(root)

# T is the tree matrix, 
# r is the root and a non-negative integer
# n1 is a node and non-negative integer
# n2 is a node and non-negative integer
# This finction return an integer
def question4(T, r, n1, n2):

	if not T or T == [[]]:
		return None
	# Build a tree from the matrix
	bst = build_tree(T, r)
	#print bst
	return lca(bst.root, n1, n2)
# Lowest Common Ancestor
def lca(N, n1, n2):
	if not N:
		return None

	cur_node = N
	if n1 > max(n1, n2):
		return lca(cur_node.left, n1, n1)
	elif n1 < min(n1, n2):
		return lca(cur_node.right, n1, n2)
	else:
		return cur_node.value




def build_tree(T, r):
	tree = BinaryTree(r)
	insert_node(T, tree.root)
	return tree
	#print 'Root: ', tree.root.value
	#print tree.root.left.value, tree.root.right.value
	#print tree.root.right.left.value



def insert_node(T, node):
	stack = [node]
	while (stack):
		new_node = None
		for index, e in enumerate(T[node.value]):
			#print e, index
			if e and index < node.value:
				new_node = node.left = TreeNode(index)
				stack.append(node.left)
				#print ' Left: of ', node.value, index
				insert_node(T, TreeNode(index))
				#return node.left
			elif e and index > node.value:
				new_node = node.right = TreeNode(index)
				stack.append(node.right)
				#print ' Right: of ', node.value, index
				insert_node(T, TreeNode(index))
				#return node.right
		return new_node
		stack.pop()
	return None


# Question 5
# Find the element in a singly linked list that's m elements from the end. 
# For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. 
# The function definition should look like question5(ll, m), 
# where ll is the first node of a linked list and m is the "mth number from the end". 
# You should copy/paste the Node class below to use as a representation of a node in the linked list. 
# Return the value of the node at that position.


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert(self, new_element, position):
        
        old_element = self.get_position(position-1)
        new_element.next = old_element.next
        old_element.next = new_element

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# ll is the first node of a linked list
# m is the mth number from the end of the linked list
def question5(ll, m):
	# Find the last element
	if not ll:
		return 0

	last = 0
	cur_node = ll.head
	while (cur_node.next):
		last = last + 1
		cur_node = cur_node.next

	index = last - m
	if index < 0:
		return None
	cur_node = ll.head
	while (index > 0):
		cur_node = cur_node.next
		index = index -1

	return cur_node.value

###################################### TESTS ######################################
###################################################################################
###################################################################################

def test_question1():
	print "Tests for Question 1: \n"

	s = "udacity"
	t = "ad"
	print "Is there an anagram of '" + t + "' in '" + s + "': "

	print question1(s,t)
	# True

	s = "udacity"
	t = ""
	print "Is there an anagram of '" + t + "' in '" + s + "': "
	print question1(s,t)
	# True

	s = "udacity"
	t = "city"
	print "Is there an anagram of '" + t + "' in '" + s + "': "
	print question1(s,t)
	# True

	s = "anagram"
	t = "nagaram"
	print "Is there an anagram of '" + t + "' in '" + s + "': "
	print question1(s,t)
	# True

	s = "anagram"
	t = "nagaram"
	print "Is there an anagram of '" + t + "' in '" + s + "': "
	print question1(s,t)
	# True

	s = "udacity"
	t = "car"
	print "Is there an anagram of '" + t + "' in '" + s + "': "
	print question1(s,t)
	# False

	print "\n"	

def test_question2():
	print "Tests for Question 2: \n"

	a = "racecar"
	print "The longest palindrome in '" + a + "' is " + " " 
	print question2(a)
	# racecar

	# Single character test
	a = "a"
	print "The longest palindrome in '" + a + "' is " + " " 
	print question2(a)
	# a

	# Empty string test
	a = ""
	print "The longest palindrome in '" + a + "' is " + " " 
	print question2(a)
	# ''

	# Empty string test
	a = "I have a racecar"
	print "The longest palindrome in '" + a + "' is " + " " 
	print question2(a)
	# racecar
	print "\n"

def test_question3():
	print "Tests for Question 3: \n"

	test = {'A': [('B', 2)],
         'B': [('A', 2), ('C', 5)], 
         'C': [('B', 5)]}

	print question3(test)
	# {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}


	test = {'A': [('B', 2)],
	          'B': [('A', 2), ('C', 5), ('D', 3)],
	          'C': [('B', 5), ('D', 3)]}
	print question3(test)
	# {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('D', 3), ('C', 5)], 'D': [('B', 3)]}

	test = {'A': [('B', 2), ('C', 1)],
	          'B': [('A', 2), ('C', 5), ('D', 3)],
	          'C': [('B', 5), ('D', 3), ('A', 1)]}
	print question3(test)
	# {'A': [('C', 1), ('B', 2)], 'C': [('A', 1), ('D', 3)], 'B': [('A', 2)], 'D': [('C', 3)]}

	test = {}
	print question3(test)
	# {}
	print "\n"

def test_question4():
	print "Tests for Question 4: \n"
	print 'Result should be 3'
	print question4([[0, 1, 0, 0, 0],
	                 [0, 0, 0, 0, 0],
	                 [0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0]],
                    3,
                    1,
                    4)
	print 'Test 2: Testing BST with LST to the right of root'
	print 'Result should be 5'
	print question4([[0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]],
                    3,
                    4,
                    6)
	print 'Test 3: Testing BST with LST to the left of root'
	print 'Result should be 1'
	print question4([[0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]],
                    3,
                    0,
                    1)


def main():
	test_question1()
	test_question2()
	test_question3()
	test_question4()
if __name__ == '__main__':
	main()