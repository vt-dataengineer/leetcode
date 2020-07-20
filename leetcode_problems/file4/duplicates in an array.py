# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]

ar = [4,3,2,7,8,2,3,1]
print(list(set([x for x in ar if ar.count(x)==2])))
