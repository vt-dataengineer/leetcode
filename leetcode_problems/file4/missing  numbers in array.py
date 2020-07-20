# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

l = [1,1]
ll = []
s = sorted(l)
print(s)
for x in s:
    if x > len(s):
        break
if len(s) == 1:
    ll.append(s+1)
else:
    for y in range(1,len(s)+1):
        if y not in s:
            ll.append(y)
print(ll)
