#Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
# where in each step you can delete one character in either string.
#Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".


s1 = 'sea'
s2 = 'eat'
count = 0
for x in s1:
    if x in s2:
        print(x)
    else:
        s1 = s1.strip(x)
        count+=1
print(count)
for x in s2:
    if x in s1:
        print(x)
    else:
        count+=1
print(count)
