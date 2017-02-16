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

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

# T is the tree matrix, 
# r is the root and a non-negative integer
# n1 is a node and non-negative integer
# n2 is a node and non-negative integer
# This finction return an integer
def question4(T, r, n1, n2):

	# Build a tree from the matrix
	bst = build_tree(T, r)

	return lca(bst.root, n1, n2)

# Lowest Common Ancestor
def lca(N, n1, n2):
	if not N:
		return None

	cur_node = N

	if cur_node.value > max(n1, n2):
		return lca(cur_node.left, n1, n2)
	elif cur_node.value < min(n1, n2):
		return lca(cur_node.right, n1, n2)
	else:
		return cur_node.value

def build_tree(T, r):
	tree = BinaryTree(r)
	insert_node(T, tree.root)

	return tree

def insert_node(T, node):
	stack = [node]
	while (stack):
		new_node = None
		#print node.value
		for index, e in enumerate(T[node.value]):
			#print e, index
			if e and index < node.value:
				new_node = node.left = Node(index)
				stack.append(node.left)

				insert_node(T, node.left)


			elif e and index > node.value:
				new_node = node.right = Node(index)
				stack.append(node.right)

				insert_node(T, node.right)

		return new_node
		stack.pop()
	return None



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
	print 'Testing BST with LST to the right of root'
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
	print 'Testing BST with LST to the left of root'
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

test_question4()













