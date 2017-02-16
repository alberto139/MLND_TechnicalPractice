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

def test2():
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

if __name__ == '__main__':
	test2()