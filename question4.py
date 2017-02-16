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
				new_node = node.left = Node(index)
				stack.append(node.left)
				#print ' Left: of ', node.value, index
				insert_node(T, Node(index))
				#return node.left
			elif e and index > node.value:
				new_node = node.right = Node(index)
				stack.append(node.right)
				#print ' Right: of ', node.value, index
				insert_node(T, Node(index))
				#return node.right
		return new_node
		stack.pop()
	return None



Matrix = [[0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [1, 0, 0, 0, 1],
          [0, 0, 0, 0, 0]]
print question4(Matrix, 3, 1, 4)













