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

def test1():
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

if __name__ == '__main__':
	test1()