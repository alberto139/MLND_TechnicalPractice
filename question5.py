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



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print question5(ll, 2)