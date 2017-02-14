# solutions.py
# Alberto G. Rivera
# February 11, 2017
# -----------------------------
# This file containes my proposed solutions to the 
# five interview questions that are part of the 
# Technical interview practice.
# Note: This file is ment to be run using python2.7 

import re # Regular Expresions


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

# Question 3
# Given an undirected graph G, find the minimum spanning tree within G. 
# A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. 
# Your function should take in and return an adjacency list structured like this:
# {'A': [('B', 2)],
# 'B': [('A', 2), ('C', 5)], 
# 'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be question3(G)
# NOTE: MST Probelm, solved with Prim's Algorithm
#import sys



def question3(G):
	import random
	MST = {}
	T = dict(G)

	# Gather the nodes to be visited
	nodes_to_visit = []
	for node in G:
		nodes_to_visit.append(node)
	#print nodes_to_visit
	visited = []

	# Pick a starting node
	#cur_node = random.choice(G.keys())
	cur_node = 'A'
	MST[cur_node] = []
	#visited.append(cur_node)

	#for edge in G[cur_node]:
	#while len(MST) < len(G):
	while len(visited) < len(G):
	#for node in G:
		visited.append(cur_node)
		print cur_node
		#cur_node = node
		#MST[node] = []
		#print G[cur_node]
		#print 'Edge: '
		#print edge
		# Look for the edge with the smallest weight that doesn't lead to a node already in the Minimum Spaning Tree
		#if edge[0] not in MST:
			# Add vertex not seen before
			#

		possible_edges = G[cur_node]
		#print 'Possible edges'
		#print possible_edges
		possible_edges = [i for i in possible_edges if i[0] not in MST]
		#print 'Possible edges'
		print possible_edges
		if not possible_edges:
			#Iterate trhough MST to se if there are any ramaining nodes
			for node in MST:
				if node not in visited:
					cur_node = node
					#if 

		smallest_edge = get_smallest_edge(possible_edges)
		print smallest_edge
		#MST[edge[0]] = []
		#MST[cur_node] = smallest_edge
		if smallest_edge:
			MST[cur_node].append(smallest_edge)
			# Add the inverse
			MST[smallest_edge[0]] = [(cur_node, smallest_edge[1])]
		#print cur_node
		#print MST
		if smallest_edge and not possible_edges:
			cur_node = smallest_edge[0]
		#print cur_node
		print MST



	return MST



#Gets the smallest edge from a given node in a graph
def get_smallest_edge(edges):
	if not edges:
		return 
	return min(edges, key=lambda t: t[1])
	



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



def tests1():
	print "Tests for Question 1: \n"

	s = "udacity"
	t = "ad"
	print "Is there an anagram of '" + t + "' in '" + s + "': "
	print question1(s,t)

	s = "udacity"
	t = ""
	print "Is there an anagram of '" + t + "' in '" + s + "': "
	print question1(s,t)

	s = "udacity"
	t = "city"
	print "Is there an anagram of '" + t + "' in '" + s + "': "
	print question1(s,t)

	s = "anagram"
	t = "nagaram"
	print "Is there an anagram of '" + t + "' in '" + s + "': "
	print question1(s,t)

	s = "anagram"
	t = "nagaram"
	print "Is there an anagram of '" + t + "' in '" + s + "': "
	print question1(s,t)

	s = "udacity"
	t = "car"
	print "Is there an anagram of '" + t + "' in '" + s + "': "
	print question1(s,t)

	print "\n"

def tests2():
	print "Tests for Question 2: \n"

	a = "racecar"
	print "The longest palindrome in '" + a + "' is " + " " 
	print question2(a)

	# Single character test
	a = "a"
	print "The longest palindrome in '" + a + "' is " + " " 
	print question2(a)

	# Empty string test
	a = ""
	print "The longest palindrome in '" + a + "' is " + " " 
	print question2(a)

	# Empty string test
	a = "I have a racecar"
	print "The longest palindrome in '" + a + "' is " + " " 
	print question2(a)
	print "\n"

def test3():
	print "Tests for Question 3: \n"

	graph = {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
	print question3(graph)

	print "\n"

	graph = {}
	print question3(graph)

	print "\n"

	graph = {'A': [('B', 2)],
			 'B': [('A', 2), ('C', 5), ('D', 10)], 
 			 'C': [('B', 5), ('D', 1)],
 			 'D': [('B', 10), ('C',1)]}
	print question3(graph)

	print "\n"

#tests1()
#tests2()
test3()
#a = "racecar"
#b = "123456789876543211"
#print isPalindrome(a)