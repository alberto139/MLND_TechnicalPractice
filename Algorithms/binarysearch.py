"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    pivot = len(input_array)/2
    
    end = len(input_array) - 1
    start = 0
    while (start <= end):

        if (input_array[pivot] == value):
            return pivot
        elif (input_array[pivot] < value):
            start = pivot + 1
            pivot = (start + end) /2

        elif (input_array[pivot] > value):
            end = pivot -1
            #pivot = len(input_array[start:end])/2
            pivot = (start + end) /2
       
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 16
#test_val2 = 19
print 'Should print 6'
print binary_search(test_list, test_val1)
#print binary_search(test_list, test_val2)