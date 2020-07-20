# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

l =  [2,0,2,1,3,1,0]
mini = l.count(min(l))
print(mini)
maxi = l.count(max(l))
print(maxi)

print(str(min(l))*mini)

print(str(max(l))*maxi)
