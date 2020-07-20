# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

l = [4,3,2,1]
z = ''
l1 = []
for x in l:
    z = str(z)+str(x)
print(z)
add = int(z)+1
for y in str(add):
    l1.append(y)
print(l1)


