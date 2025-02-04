# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3

def majority_count(array):
    counter=0
    majority_element=0
    for i in array:
        if counter==0:
            majority_element=i
        if majority_element==i:
            counter+=1
        else:
            counter-=1
    return majority_element
