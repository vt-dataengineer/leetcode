# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
#              (3,6) or (6,9) has the maximum difference 3.
if __name__=='__main__':
    l = [3,6,9,1]
    so = sorted(l)
    print(so)
    d = []

    for x in range(len(l)-1):
        d.append(l[x+1]-l[x])


print(max(d))
