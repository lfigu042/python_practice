# 1.1 Is Unique question
# Implement an algorithm  to determine if a string has all unique characters


def is_unique(string_test):
    a_set = set()
    for char in string_test:
        if char not in a_set:
            a_set.add(char)
        else:
            return False
    return True

print(is_unique("hello"))
print(is_unique('howdy'))

'''
Problem: Check if string has unique characters
Example: "hello" -> False
         "hey" -> True

Solution:
Created a set and keep track of every character as I
loop through the string. When I encounter a character
that is already in the set, I return False because if its
already in the set, then its not Unique.
Time complexity: O(N)  - N being size of string
Space complexity: O(N) - N being unique characters
'''