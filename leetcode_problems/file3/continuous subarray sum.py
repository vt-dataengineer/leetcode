# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
if __name__=='__main__':
    l = [23,4,6,2,7]
    k = 6
    s = 0
    for x in range(len(l)):
        for y in range(x+1,len(l)):
            if l[x]+l[y] == k:
                print(l[x],l[y])
                print('True')


