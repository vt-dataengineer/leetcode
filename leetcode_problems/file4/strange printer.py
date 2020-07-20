# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".

s = "abcabc"

se = set(s)
print(se)
count =0
for x in se:
    count+=1

print(count)
