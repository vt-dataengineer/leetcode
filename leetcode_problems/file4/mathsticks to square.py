# Input: [1,1,2,2,2]
# Output: true
#
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

l = [1,1,2,2,2]
print(l)
m = max(l)
c = l.count(m)
print(m,c)
for x in range(len(l)):
    if l[x] == m:



print(l)
