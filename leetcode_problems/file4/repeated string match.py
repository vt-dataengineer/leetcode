# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it.
# If no such solution, return -1.
#
# For example, with A = "abcd" and B = "cdabcdab".
#
# Return 3, because by repeating A three times (“abcdabcdabcd”),
# B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

# a = 'abcd'
# a1 = 'abcd'
# b = 'cdabcdab'
a = "abcabcabcabc"
b = "abac"

#a = "abc"
# b = "cabcabca"

# c = ''

# count = 0
#
# while b not in c:
#     c = c+a
#     print(c)
#     count+=1
#
# print(count)

print(a.lower())
